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

function submit(e) {
  console.log(e)
}