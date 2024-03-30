$(document).ready(function()
{
    $.getJSON("fetch.php",function(data)
    {
        $.each(data, function()
        {
            $("#display").append("<option value="+this['violations']+"</option>");
        });
    });
});