window.onload = () => {
  var slider = document.getElementById("brightness-slider");
  var output = document.getElementById("brightness-out");
  output.innerHTML = slider.value;

  slider.oninput = function() {
    output.innerHTML = this.value;
  };
  slider.onchange = () => {
    fetch(`/api/on/level?lightlevel=${slider.value}`, {
      method: "put"
    })
      .then(console.log)
      .catch(console.error);
  };
  // slider.onmouseup = () => {
  //   fetch(`/api/setb/${slider.value}`, {
  //     method: "post"
  //   })
  //     .then(console.log)
  //     .catch(console.error);
  // };

  const dim = document.getElementById("dim");
  const on = document.getElementById("on");
  const off = document.getElementById("off");

  on.onclick = e => {
    fetch("/api/on", {
      method: "put"
    })
      .then(console.log)
      .catch(console.error);
  };
  off.onclick = e => {
    fetch("/api/off", {
      method: "put"
    })
      .then(console.log)
      .catch(console.error);
  };
};
