now = new Date();
now_hour = now.getHours();
now_minutes = now.getMinutes();
now_seconds = now.getSeconds();

now_time_secs = (now_hour * 60 * 60) + (now_minutes * 60) + now_seconds

auctions = $('.auctions');
interval_id = new Object();

custom_clearInterval = function (id, a){
	clearInterval(interval_id[id])
}

formatState = function (state) {
  if (state.id) { 
	  var $state = $(
	    '<span><img src="'+state.id+'" class="img-flag" height="30" width="32"/> ' + state.text + '</span>'
	  );
  }
  else {
  	var $state = $(state.text);
  }

  return $state;
};

post_auction_info = function (bid_btn, bid_amt, member_id, chit_id) {
	$(bid_btn).on('click', function () {
		$(this).prop('disabled', true);
		fdata = JSON.stringify({'bid_amt': bid_amt, 'mid': member_id, 'chit_id': chit_id})
	  	$.ajax({
		    url: '/record/auctions/',
		    method: 'post',
		    data: {'data': fdata},
		    complete: function(result, status) {
		    	response = JSON.parse(result.responseText)
		      if (response['status'] == 'success'){
		      	window.location.reload();
		      }
		      else {
		      	alert(result.responseText);
		      }
		    }
		 });
	});
}

show_members_util = function (m_id){
	id = m_id.split('-')[0]
	$('#'+id+'-bidder').parents('.bidder-container').show();
	
	$('#'+id+'-bidder').select2({templateResult: formatState}).on("change", function(e) {
		member_id = $($('#'+id+'-bidder').select2('data')[0].element).attr('data-id')
		bid_btn = $('#'+id+'-bid-complete-btn') 
		bid_btn.removeAttr('disabled');
		bid_amt = $('#'+m_id).find('#latest-bid').text()
		post_auction_info(bid_btn, parseInt(bid_amt), parseInt(member_id), parseInt(m_id))

	});
}

show_members_to_select = function (m_id){
	if ($('#'+m_id).is(':visible')){
		show_members_util(m_id)
	}
	else {
		$('#'+m_id).on('shown.bs.modal', function (){
			show_members_util(m_id)
	    });
	}
}


bid_timer = function (rm, rs, modal_id){
	return setInterval(function(){
		
		if (rm ==0 && rs ==0){
			$('#'+modal_id).find('.bid-input-form').remove();
			show_members_to_select(modal_id)
			custom_clearInterval(modal_id)
		}

		else if (rs == 0){
			rs = 59;
			rm = rm -1
		}

		else if (rs > 0){
			rs = rs -1
		}

		if (String(rm).length < 2){
			rm = '0'+String(rm)
		}

		if (String(rs).length < 2){
			rs = '0'+String(rs)
		}
		$('#'+modal_id).find('#bid-counter').empty().append(rm+':'+rs)

	}, 1000);
}


for (i=0; i<auctions.length; i++){
	var auction = auctions[i];
	var int_id = auction.id
	var start_time = $(auction).find('input').val().split(':');
	var start_hour = start_time[0];
	var start_minute = start_time[1];
	var start_time_secs = (parseInt(start_hour) * 60 * 60) + (parseInt(start_minute) * 60);
	var remaining_time_secs = start_time_secs - now_time_secs;
	var remaining_hours = parseInt(remaining_time_secs/3600) % 24;
	var remaining_minutes = parseInt(remaining_time_secs/60) % 60;
	var remaining_seconds = remaining_time_secs % 60;

	timer = function (remaining_seconds, remaining_minutes, remaining_hours, auction){
		return setInterval(function(){
			var id = auction.id;
			if (remaining_seconds > 0){
				remaining_seconds = remaining_seconds -1
			}

			else if (remaining_minutes > 0){
				remaining_minutes = remaining_minutes -1
				remaining_seconds = 59;
			}
			else if (remaining_seconds == 0 && remaining_minutes == 0 && remaining_hours != 0){
				remaining_hours = remaining_hours - 1
				remaining_seconds = 59;
				remaining_minutes = 59;
			}
			else if (remaining_hours <= 0 ){
				$('#'+auction.id+"-bid-btn").show();
				$(auction).find('div.display_remaining_time').hide()
				custom_clearInterval(id);
			}
			var rtime = String(remaining_hours)+':'+String(remaining_minutes)+':'+String(remaining_seconds)
			$(auction).find('div.display_remaining_time').empty().append(String(rtime))
		}, 1000);
	}
	interval_id[int_id] = timer(remaining_seconds, remaining_minutes, remaining_hours, auction);
}


$('div.auctions').on('click', 'button', function (){
	console.log('bul')
	var id = this.id.split('-')[0]
	$('#'+id+'-bid-modal').modal('show');
});


$('.bid-input-form').submit( function (event){
	event.preventDefault();
	modal_id = $(this).parents('.modal')[0].id
	custom_clearInterval(modal_id)
	interval_id[modal_id] = bid_timer(1, 0, modal_id);
	input_id = $(this).parent().find('input')[0].id
	latest_bid = $(this).parents('.modal').find('#latest-bid')
	latest_bid.empty().append($('#'+input_id).val())
	$('#'+input_id).val(null);
});


$('.modal').on('shown.bs.modal', function (){
	_id = this.id
	if (!(_id in interval_id)){
		remaining_time = $(this).find('#bid-counter').text();
		rt = remaining_time.split(':')
		rm = parseInt(rt[0])
		rs = parseInt(rt[1])

		if ((rm != 0 && rs != 0) || rm != rs){
			interval_id[_id] = bid_timer(rm, rs, _id)
		}
	}
});
