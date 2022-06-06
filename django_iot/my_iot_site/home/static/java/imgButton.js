function getPage(page_name) {
    if(page_name == '' | page_name == 'home'){
        document.location.href="/";
    } else {
        location.replace(page_name)
    }
}
