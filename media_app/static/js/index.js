let date=document.getElementById('date')
function tick(){
    return (date.innerText=new Date().toUTCString()).substring(10,14)
}
setInterval(tick,1000)

