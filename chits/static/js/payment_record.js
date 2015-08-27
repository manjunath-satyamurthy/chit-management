$(document).ready( function () {
  if (window.location.search != ''){
    $('.payment_checkbox').removeAttr('checked');
    $('#payment_record_table').DataTable({
      "bLengthChange" : false,
      "columnDefs": [
        { "width": "10%", "targets": [3],
        }
      ],
    });
  }
  else {

    $('select#select_chitbatch').select2().on("change", function(e) {
      id = $('#select_chitbatch').val()
      activate_select_date(id)
    });
  }

});


activate_select_date = function (id) {
  options = $('div.bid_date_select').find('#'+id).html()
  $('#select_bid_date').empty().append(options);
  $('.bid_date').show();
  $('#select_bid_date').select2().on("change", function(e) {
    bid_date = $('#select_bid_date').val()
    console.log(id);
    window.location.href = window.location.href+'?id='+id+'&'+'bid_date='+bid_date 
  });

}

$('.payment_checkbox').on('click', function () {
  if ($('.payment_checkbox:checked').length != 0){
    $('#check_paid_btn').show();
  }
  else {
    $('#check_paid_btn').hide(); 
  }
});

$('#check_paid_btn').on('click', function (){
  ids = []
  checked = $('.payment_checkbox:checked')
  for (i=0; i<checked.length; i++){
    ids.push(parseInt(checked[i].value))
  }
  fdata = JSON.stringify(ids)

  $.ajax({
    url: '/record/payments/',
    method: 'post',
    data: {'data': fdata},
    complete: function(result, status) {
      window.location.reload();
    }
  });

});