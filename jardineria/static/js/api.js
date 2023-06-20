function iniciarMap(){
    var coord = {lat:-33.4997031 ,lng: -70.7581663};
    var map = new google.maps.Map(document.getElementById('map'),{
      zoom: 15,
      center: coord
    });
    var marker = new google.maps.Marker({
      position: coord,
      map: map
    });
}