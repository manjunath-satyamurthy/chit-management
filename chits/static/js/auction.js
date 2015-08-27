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
				$('#'+auction.id+"_bid_btn").show();
				$(auction).find('div.display_remaining_time').hide()
				custom_clearInterval(id);
			}
			var rtime = String(remaining_hours)+':'+String(remaining_minutes)+':'+String(remaining_seconds)
			$(auction).find('div.display_remaining_time').empty().append(String(rtime))
		}, 1000);
	}
	interval_id[int_id] = timer(remaining_seconds, remaining_minutes, remaining_hours, auction);
}
