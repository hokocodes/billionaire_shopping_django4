
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
window.onload = function() {
    $.ajax({
        type: "POST",
        url: "",
        data: {
         value: 'loaded',
         csrfmiddlewaretoken: csrftoken
        },
      });  //example function call.
  }