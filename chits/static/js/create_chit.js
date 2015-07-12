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

  $('#myModal').on('show.bs.modal', function(e){
    setTimeout( function(){
      member_table.columns.adjust();
      return null;
    }, 200);

  });

});