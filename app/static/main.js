window.onload = () => { 
  
  setInterval(function () {
    fetch('/api/moistureout', {
      method: 'GET'})
      .then(response => response.json())
      .then(data =>{
        document.getElementById('moisturefield').innerHTML=data.moisture;
      })
  }, 8000)

  document.getElementById("brightness-slider").onchange = (e) => {
    console.log(e)
    fetch(`/api/on/level?lightlevel=${e.currentTarget.value}`, {method: 'PUT'})
  }
};


function disco(){
  box = document.getElementById('discotoggle')  
  if(box.checked){
    window.interval = setInterval(function () {
      if(box.checked){
        fetch('/api/ciscodisco/on', {method: 'PUT'});
      }
      else{
        clearInterval(window.interval);
        window.interval = null;
      }
    }, 20000);
  }
  else{
    clearInterval(window.interval);
    window.interval = null;
  }
  
}
function submit(e) {
  console.log(e);
}