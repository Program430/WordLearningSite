class Table{
    static table = document.querySelector('.box ul');
    
    static addWord(word){
        const li = document.createElement('li');
        li.textContent = word;
        this.table.appendChild(li);
    }
    
    static clearTable(){
        this.table.innerHTML = '';
    }

    static addWords(wordList){
        for (let i = 0 ; i < wordList.length; i++){
            this.addWord(wordList[i]);
        }
    }

    static addListenerForEachElement(){
        this.table.querySelectorAll('li').forEach(item => {
            item.addEventListener('click', () => {
                window.location.href = `${serverUrl}/word_card/${item.textContent}`;
            });
        });
    }

    static async getListFromServer(pageNumber) {
        const url = `${serverUrl}/word_list/${pageNumber}/`;
        const response = await fetch(url);
        const data = await response.json();
        return data.word_list; 
    }
}

function setPageNumber(number){
    const pageNumberTitle = document.querySelectorAll('.box h2')[0];
    pageNumberTitle.innerText = `Page namber is ${number}`
  }
  

async function mainTable(){
    let lastPageNumber = Number(localStorage.getItem('lastPageNumber')) || 1;
    localStorage.setItem('lastPageNumber', lastPageNumber);
    setPageNumber(lastPageNumber);
    Table.clearTable(); 
    let wordList = await Table.getListFromServer(lastPageNumber);
    Table.addWords(wordList);
    Table.addListenerForEachElement();
}

class MyTable extends Table {
    static async getListFromServer(pageNumber) {
        const url = `${serverUrl}/word_list/${pageNumber}/`;
        const response = await fetch(url);
        const data = await response.json();
        return data.word_list; 
    }
}



mainTable();
