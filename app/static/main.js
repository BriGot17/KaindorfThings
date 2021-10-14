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
  runAsync(() => {
    while(box.checked){
      fetch('/api/ciscodisco/on', {method: 'PUT'})
      wait(20000)
      box = document.getElementById('discotoggle')
    }
  })
  console.log("123");

}

async function runAsync(callback) {
  callback();
} 

function wait(ms)
{
  var start = new Date().getTime();
  var end = start;
  while(end < start + ms){
    end = new Date().getTime();
  }
}
function submit(e) {
  console.log(e);
}