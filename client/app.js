function onpageload(){
    console.log("document loaded");
    var url="https://127.0.0.1:5000/get_location_names"; 
    $.get(url,function(data,status){
        data=['dhf df','ola nagar','rajener chokew','kd hfdh f']
        if(data){
            var locations=data.locations;
            var uil=document.getElementById("uil");
            $('#uil').empty();
            for(var i in locations){
                var opt=new Option(locations[i]);
                $('uil').append(opt);
            }
        }

    });

}
window.onload=onpageload()