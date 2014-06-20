// Run in Chrome's Developer Tools Console: Crtl+Shift+I

var playlist = document.querySelectorAll('.song-table tr.song-row');
for(var i =0; i<playlist.length ; i++) { 
  var l = playlist[i]; 
  var title = l.querySelectorAll('td[data-col="title"] .content')[0].textContent;
  var artist = l.querySelectorAll('td[data-col="artist"] .content')[0].textContent;
  console.log(artist.replace(","," ") + ',' + title.replace(","," ")); //take out "," to clean up CSV
  
}