

(async function() {
    v = 3.7;
    // check prior inclusion and version
    if (window.jQuery === undefined || window.jQuery.fn.jquery < v) {
        var done = false;
        var script = document.createElement("script");
        script.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.7.1/jquery.min.js";
        script.onload = script.onreadystatechange = function(){
            if (!done && (!this.readyState || this.readyState == "loaded" || this.readyState == "complete")) {
                done = true;
                initMyBookmarklet();
            }
        };
        document.getElementsByTagName("head")[0].appendChild(script);
    } else {
        initMyBookmarklet();
    }

    function initMyBookmarklet() {
        (window.myBookmarklet = function() {
            // your JavaScript code goes here!
            // window.open("/", "popup", "width=500,height=300");
            const element = document.getElementsByTagName("p");
            element[0].innerHTML = window.location.href;
            
                
            if (csrfTokenElement) {
                const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
                
                $.ajax({
                    url: '',
                    type: 'POST',
                    data: {
                        url: window.location.href,
                        csrfmiddlewaretoken: csrftoken
                    },
                    success:function(data){ 
                        window.myBookmarklet.imagesCallback = function(bookimgs) {
                            console.log('Fetched images:', bookimgs);
                            // Update the page here
                        };
                
                        // Call the newly defined function
                        window.myBookmarklet.imagesCallback(data.bookimgs);
                        window.location = '';
                    }
                });
            } else {
                console.error('CSRF token element not found.');
            }
            
            
        })();
    }
    // alert(window.location.href);

    
})();

