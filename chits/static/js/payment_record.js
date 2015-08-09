$(document).ready( function () {
  if (window.location.search != ''){
    console.log('here');
    $('#payment_record_table').DataTable({
      "bLengthChange" : false,
    });
  }
  else {

    $('select').select2().on("change", function(e) {
      id = $('#select_chitbatch').val()
      window.location.href = window.location.href+'?id='+id 

    });
  }

});

// $('#select_chitbatch').change(function (){
//   console.log('here');
// })

