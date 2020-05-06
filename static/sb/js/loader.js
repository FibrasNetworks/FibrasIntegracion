function cargar(){
    document.body.style.animationName = 'elim';
    setTimeout(() => {
            document.getElementsByClassName('loader')[0].style.display = 'none';
            document.getElementById('link').href = "{% static 'sb/css/style-loader.css'%}"
    })
}