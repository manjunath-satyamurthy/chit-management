$(document).ready( function () {
  $('#datetimepicker1').datetimepicker({
    step: 30,
  });

  member_table = $('#add_members').DataTable({
    "bLengthChange" : false,
    "columnDefs": [
     { "width": "2%", "targets": [0] }
    ],
    "scrollY": "250px",
    "scrollCollapse": true,
    "paging": false,
    "bInfo": false,
  });

  $('#create_chit_form').validator();

  $('#create_chit_submit').click( function (e) {
    console.log('cathed')
    e.preventDefault();
    $('#create_chit_form').validator('validate');
  });

});

$('#add_members_button').click( function (e) {
  e.preventDefault();
  $('#create_chit_form').validator('validate');
  if ($('#no_members').hasClass('has-error') == true) {
    console.log('no here')
  }

  else {
    console.log('here')
    $('#myModal').modal();
  }
});

$('#myModal').on('show.bs.modal', function(e){
  setTimeout( function(){
    member_table.columns.adjust();
    return null;
  }, 200);
});