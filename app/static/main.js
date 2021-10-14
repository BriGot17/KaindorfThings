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