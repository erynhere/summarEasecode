// document.write("hello");
var url = "";

function showText(data) {
  document.getElementById('textdisplay').innerText = data;
}

document.getElementById("btn").onclick = function() {
  let url = "";
  // document.write("btn clicked");
  chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
      url = tabs[0].url;
      // document.write(encodeURIComponent(url));

      APIurl = "https://webscrapingapi-393504.uw.r.appspot.com/getText?url=" + encodeURIComponent(url);
      // document.write("next line");
      // document.write(APIurl);
      fetch(APIurl).then(res => res.json()).then(data => showText(data));
    });

    /*
  APIurl = "https://webscrapingapi-393504.uw.r.appspot.com/getText?url=" + encodeURIComponent("https://www.tutorialspoint.com/tableau_online_training/index.asp");
  document.write("next line");
  APIurl = url;
  document.write(APIurl);
  // console.log()
  // fetch("https://webscrapingapi-393504.uw.r.appspot.com/getText?url=https%3A%2F%2Fwww.tutorialspoint.com%2Ftableau_online_training%2Findex.asp").then(res => res.json()).then(data => document.write(data));  
  fetch(APIurl).then(res => res.json()).then(data => document.write(data));
  */
};
//chrome.addEventListener('DOMContentLoaded', function () {
  //  chrome.tabs.query({active: true, lastFocusedWindow: true}, tabs => {
    //    let url = tabs[0].url;
      //  document.write(url);
        // use `url` here inside the callback because it's asynchronous!
    //});
//});