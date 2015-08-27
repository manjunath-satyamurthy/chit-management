$(document).ready( function () {
  $('#datetimepicker1').datetimepicker({
    step: 30,
    theme:'dark',
    format:'d.m.Y H:i'
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

});

post_to_create_chit = function () {

  chit_members_id = []
  members = $('.members:checked')

  for (i=0; i<members.length; i++){
    chit_members_id.push(members[i].id)
  }

  raw_datetime = $('input[name=datetime]').val().split(' ')
  date = raw_datetime[0].split('.');
  time = raw_datetime[1].split(':');

  datetime = {
    'dd': parseInt(date[0]),
    'mm': parseInt(date[1]),
    'yyyy': parseInt(date[2]),
    'h': parseInt(time[0]),
    'm': parseInt(time[1]),
  }

  fdata = JSON.stringify({
      name:$('input[name=name]').val(),
      principal: parseInt($('input[name=principal]').val()),
      period: parseInt($('input[name=period]').val()),
      no_of_members: parseInt($('input[name=members_count]').val()),
      datetime: datetime,
      chit_members_id: chit_members_id
  });

  $.ajax({
    url: '/chits/create/',
    method: 'post',
    data: {'data': fdata},
    complete: function(result, status) {
      response = JSON.parse(result.responseText)
      if (response['status'] != "success"){
        alert(response['message']);
      }
      alert(response['status']);
      window.location.reload();
    }
  });

}

$('#create_chit_submit').click( function (e) {
  e.preventDefault();
  $('#create_chit_form').validator('validate');
  if ($('#no_members').hasClass('has-error') == false) {
    post_to_create_chit();     
  }
});

$('#add_members_modal_button').click( function (e) {
  e.preventDefault();
  $('#create_chit_form').validator('validate');
  if ($('#no_members').hasClass('has-error') == true) {
  }

  else {
    console.log('here')
    console.log()
    $('#members_count').empty().append(
      $('#no_members_input').val() - $('.members:checked').size()
    );
    $('#myModal').modal();
  }
});

var limit=0;

$('#myModal').on('show.bs.modal', function(e){
  limit = $('#no_members_input').val();
  setTimeout( function(){
    member_table.columns.adjust();
    return null;
  }, 200);
});

$('.members').click(function (){
  $('#members_count').empty().append(
    $('#no_members_input').val() - $('.members:checked').size()
  );
});

$('#myModal').on('hide.bs.modal', function (e) {
  $('.members:checked')
});

$('input.members').on('change', function(evt) {
   if($('.members:checked').size() > limit) {
      this.checked = false;
   }
});

$('#add_members_button').click(function () {
  members = $('.members:checked');
  images = ""
  if (members.length > 0){
    for (i=0; i<members.length; i++){
      img_id = '#img_'+ String(members[i].id)
      images = images.concat($(img_id).html())
    }
    $('.selected_members').empty().append(images)
    $('#myModal').modal('hide');
  } 

  else {
    $('.selected_members').empty().append('None');
    $('#myModal').modal('hide');
  }

});