(function() {
 console.log('here')
 let form = document.querySelector('.subscribe-form');
 form.addEventListener('submit',async (event) => {
   event.preventDefault();
   console.log(form.email.value);
   let postData = {
    "email": form.email.value
   }
   let response = await fetch('http://127.0.0.1:8000/api/subscribers/', {
    headers: {
        'X-CSRFToken': getCookie("csrftoken"),
        'Content-Type': 'application/json',
        },
    method: 'POST',
    body: JSON.stringify(postData)
   })

   form.email.value = '';
   let responseData = await response.json();
   if(response.ok){
    alert('Uğurla Subscribe oldunuz')
   }else{
    alert(responseData.email)
   }

 });

})();