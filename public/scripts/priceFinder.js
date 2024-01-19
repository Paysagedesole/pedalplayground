let request = new XMLHttpRequest();
request.open("GET", "https://reverb.com/p/jhs-morning-glory-v4", true);
request.onload = () => {
  const doc = new DOMParser().parseFromString(request.responseText, 'text/html');
  document.querySelector('#content').innerHTML = doc.getElementsByClassName('price-display')[0].innerHTML;
}
window.onload = function(){
    var name = prompt("What's your name?");
    var lengthOfName = name.length

    document.getElementById('testVariable').innerHTML = lengthOfName;}
request.send();