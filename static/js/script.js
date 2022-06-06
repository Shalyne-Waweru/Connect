$(document).ready(function(){
  $('.pic-upload').hide();

  $('#change-profile-btn').click(function(){
    $('.pic-upload').toggle();
  })

  $('.close').click(function(){
    $('.alert').css("display", "none");
  })

});