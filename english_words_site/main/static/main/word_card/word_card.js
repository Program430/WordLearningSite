let arrow = document.getElementById('back');
const csrftoken = document.getElementById('csrf-token').value;

/////////////////////

let add_or_create = document.getElementById('add_or_create');
let func_name = undefined;
let eng_word = document.querySelector('.description h2');

async function addOrDeleteFunction(word){
    let url = (!func_name) ? `${serverUrl}/user_word_list/add/` : `${serverUrl}/user_word_list/delete/`
    let response = await fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'english': word}),
      });
    func_name = !func_name;
    return await response.json();
}

async function setAddOrDelete(word){
    let response = await fetch(`${serverUrl}/user_word_list/check/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'english': word}),
      });
      response = await response.json();
      console.log(response);
    if (response.statusB === 'Yes'){
        func_name = true;
    }
    if (response.statusB === 'No'){
        func_name = false;
    }
}

async function changeButton(){
    if (func_name){
        add_or_create.textContent = 'Delete';
    }else{
        add_or_create.textContent = 'Add';
    }
}

add_or_create.addEventListener('click', async () => {
    let word = eng_word.textContent; 
    await addOrDeleteFunction(word);
    await changeButton();
});

async function main(){
    let word = eng_word.textContent; 
    await setAddOrDelete(word);
    await changeButton();
}

main();