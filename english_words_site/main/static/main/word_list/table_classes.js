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
                if (document.title == 'My words'){
                    window.location.href = `${serverUrl}/word_card/${item.textContent}/mylist/`;
                }
                else{
                    window.location.href = `${serverUrl}/word_card/${item.textContent}/list/`;
                }
            });
        });
    }

    static async getListFromServer(pageNumber) {
        const url = `${serverUrl}/word_list/${pageNumber}/`;
        const response = await fetch(url);
        const data = await response.json();
        return data.word_list; 
    }

    static async page_count(){
        const url = `${serverUrl}/word_list/count/`;
        const response = await fetch(url);
        const data = await response.json();
        return data.count; 
      }
      
}

function setPageNumber(number){
    const pageNumberTitle = document.querySelectorAll('.box h2')[0];
    console.log(pageNumberTitle);
    pageNumberTitle.innerText = `Page namber is ${number}`
  }
  
async function mainTable(pageNumber){
    Table.clearTable(); 
    let wordList = await Table.getListFromServer(pageNumber);
    Table.addWords(wordList);
    Table.addListenerForEachElement();
}

