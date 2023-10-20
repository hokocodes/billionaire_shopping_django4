(async function() {

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
            const element = document.getElementsByTagName("p");
            element[0].innerHTML = window.location.href;
        
            $.ajax({
                url: '',
                type: 'get',
                data: {
                    url: window.location.href
                },
                success: function(){
                    window.open('/');
                }
            });
        })();
    }
    // alert(window.location.href);

    
})();

