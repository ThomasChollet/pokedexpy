const searchForm = document.querySelector("#searchForm")

function retrieve(event){
    event.preventDefault();
    const data = new FormData(searchForm);
    const xhr = new XMLHttpRequest();

    xhr.open("POST", '/search', true);
    xhr.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhr.send(JSON.stringify(Object.fromEntries(data)))
    xhr.onload=function(){
        document.querySelector("#results").innerHTML = this.responseText
    }

}

searchForm.addEventListener('submit', retrieve)