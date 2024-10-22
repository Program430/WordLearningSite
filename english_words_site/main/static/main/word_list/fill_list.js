const hereLocation = window.location.href;
const url = new URL(hereLocation);
const serverUrl = url.origin;

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

    static async getListFromServer(pageNumber) {
        const url = `${serverUrl}/word_list/${pageNumber}/`;
        const response = await fetch(url);
        const data = await response.json();
        return data.word_list; 
    }
}

(async () => {
    let wordList = await Table.getListFromServer(1);
    console.log(wordList);
    console.log('llllllllllll' + wordList.length);
    Table.addWords(wordList);
})();