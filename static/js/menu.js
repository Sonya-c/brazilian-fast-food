function dashboard()
{
    alert( "dashboard" )
    // document.getElementById( "main-content-inner" ).appendChild( "dashboard.html" );

    var html = "dashboard.html";

    /*insert the html in a new element
    you could use a different parent tag, but I chose the span tag*/

    var newElement = document.getElementById('main-content-inner');
    newElement.innerHTML = html;

    //add the html to the document before the script element
    var thisScript = document.currentScript;
    thisScript.parentElement.insertBefore(newElement, thisScript);
}

