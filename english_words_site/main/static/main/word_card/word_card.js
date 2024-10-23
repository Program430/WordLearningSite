let arrow = document.getElementById('back');


function returnFunction(){
    window.location.href = `${serverUrl}/word_list/`;
}

arrow.addEventListener('click', returnFunction);