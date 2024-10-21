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
                alert('Элемент "' + item.textContent + '" был нажат!');
            });
        });
    }

    static getListFromServer(){

    } 

}

Table.addWord('Ndsdsad');