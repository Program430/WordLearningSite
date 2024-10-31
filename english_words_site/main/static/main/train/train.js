let words = [
    
];

let mixedAnswers = [
    
];

let currentWordIndex = 0;

async function getDataList(){
    let result = await fetch(`${serverUrl}/get_train_data_full_list/`);
    mixedAnswers =await result.json();
    mixedAnswers = mixedAnswers['data'];
}

async function getDataUserList(){
    let result = await fetch(`${serverUrl}/get_train_data_user/`);
    words = await result.json();
    words = words['data'];
}

async function main(){
    await getDataList()
    await getDataUserList();
    loadQuestion();
}

async function loadQuestion() {
    const questionContainer = document.getElementById("question");
    const answersContainer = document.getElementById("answers");
    const resultContainer = document.getElementById("result");
    const nextButton = document.getElementById("next-button");

    resultContainer.innerText = "";
    nextButton.style.display = "none"; // Скрыть кнопку "Следующий вопрос"

    const word = words[currentWordIndex];
    questionContainer.innerText = `Переведите слово: ${word.en}`;

    const correctTranslation = word.ru;
    let answers = [correctTranslation];

    // Добавляем неправильные ответы
    while (answers.length < 4) {
        const randomAnswer = mixedAnswers[Math.floor(Math.random() * mixedAnswers.length)].ru;
        if (!answers.includes(randomAnswer)) {
            answers.push(randomAnswer);
        }
    }

    // Перемешиваем ответы
    answers = answers.sort(() => Math.random() - 0.5);

    answersContainer.innerHTML = answers.map(answer => `
        <div class="answer" onclick="checkAnswer('${answer}', '${correctTranslation}')">
            ${answer} <a href="${serverUrl}/word_card/${word.en}/trainlist">🔗</a>
        </div>
    `).join('');

    if (currentWordIndex >= words.length - 1) {
        currentWordIndex = 0;
        await getDataList();
        await getDataUserList();
 
        return;
    }
}

function checkAnswer(selected, correct) {
    const resultContainer = document.getElementById("result");
    const nextButton = document.getElementById("next-button");

    if (selected === correct) {
        resultContainer.innerText = "✅ Правильно!";
    } else {
        resultContainer.innerText = "❌ Неправильно. Правильный ответ: " + correct;
    }

    nextButton.style.display = "block"; // Показать кнопку "Следующий вопрос"
    currentWordIndex++;
}


main();