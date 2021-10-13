window.onload = () => { 
  setInterval(function () {
    fetch('/api/moistureout', {
      method: 'GET'})
      .then(response => response.json())
      .then(data =>{
        console.log(data)
        document.getElementById('moisturefield').innerHTML=data.moisture;
      })
  }, 10000)
};
