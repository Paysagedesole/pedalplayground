window.onload = function()
			{
                let request = new XMLHttpRequest();
                request.open("GET", "https://reverb.com/p/epiphone-firebird-2020-present", true);
                request.onload = () => 
                {
                    
                    const doc = new DOMParser().parseFromString(request.responseText, 'text/html');
                    document.getElementById('testVariable').innerHTML = doc.getElementsByClassName('price-display')[0].innerHTML;
                }
          
                request.send();
            }
