$(document).ready(function(){
  var form = $('#form_buying_product');
  console.log(form);
  form.on('submit',function(e){
    e.preventDefault();

  });

  function showingbasket(){
    $('.basket-items').toggleClass('hidden')
  }

  $('.basket-container').mouseover(function(){
    showingbasket();
  })
  $('.basket-container').mouseout(function(){
    showingbasket();
  })
});
