qu_captcha = {};
qu_captcha.form = document.querySelector('.qu-captcha-form');
if (!qu_captcha.form) {
    throw new Error("No form to load CAPTCHA");

}
qu_captcha.uses_cookie = qu_captcha.form.classList.contains('qu-captcha-uses-cookie');
qu_captcha.url = qu_captcha.form.getAttribute('src').replace('/get_api', '');

qu_captcha = {};
qu_captcha.form = document.querySelector('.qu-captcha-form');
if (!qu_captcha.form) {
    throw new Error("No form to load CAPTCHA");
}
qu_captcha.uses_cookie = qu_captcha.form.classList.contains('qu-captcha-uses-cookie');
qu_captcha.url = qu_captcha.form.getAttribute('src').replace('/get_api', '');

const style = document.createElement('style');
style.textContent = `
    .qu-captcha-reset-style, .qu-captcha-reset-style * {
        all: initial;
        font-family: Arial, sans-serif;
    }
    .qu-captcha-container {
        margin: 0 auto;
        width: min-content;
        min-width: 150px;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 5px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
        background-color: #e5ebf8;
        text-align: center;
        border: 1px solid black;
    }
    .qu-captcha-image {
        margin: 5px 0;
        border: 1px solid black;
        width: min-content;
    }
    .qu-captcha-hidden {
        display: none;
    }
    .qu-captcha-gray-button {
        text-align: center;
        min-width: min(40vw, 7vh);
        max-width: 230px;
        padding: 10px;
        border-radius: 4px;
        cursor: pointer;
        color: white;
        font-size: 16px;
        border: 1px solid #707070;
        background-color: #a0a0a0;
    }
    .qu-captcha-gray-button:hover {
        background-color: #707070;
    }
    .qu-captcha-button {
        text-align: center;
        min-width: min(40vw, 7vh);
        max-width: 230px;
        padding: 10px;
        border: none;
        border-radius: 4px;
        cursor: pointer;
        background-color: #007bff;
        color: white;
        font-size: 16px;
    }
    .qu-captcha-button:hover {
        background-color: #0056b3;
    }
    .qu-captcha-button-group {
        width: 100%;
        display: flex;
        gap: 10px;
        justify-content: space-between;
    }
    .qu-captcha-p {
        margin: 5px 0;
        font-family: Arial;
        text-align: left;
    }
    .qu-captcha-loading {
        margin: 0 0 5px 0;
        display: none;
        width: 40px;
        height: 40px;
        border: 4px solid #ccc;
        border-top-color: #0056b3;
        border-radius: 50%;
        animation: qu-captcha-spin 1s linear infinite;
    }
    @keyframes qu-captcha-spin {
        to {
            transform: rotate(360deg);
        }
    }
`;

qu_captcha.div = document.createElement('div');
qu_captcha.shadow = qu_captcha.div.attachShadow({ mode: 'open' });

qu_captcha.shadow.appendChild(style);

qu_captcha.container = document.createElement('div');
qu_captcha.container.className = 'qu-captcha-container qu-captcha-reset-style';

qu_captcha.instruction = document.createElement('p');
qu_captcha.instruction.className = 'qu-captcha-p';
qu_captcha.instruction.textContent = 'На рисунке несколько отрезков и одна ломаная. Расставьте точки в порядке следования вершин ломаной';

qu_captcha.min_dimension = Math.min(window.screen.width, window.screen.height, 300)
qu_captcha.canvas = document.createElement('canvas');
qu_captcha.canvas.className = 'qu-captcha-image qu-captcha-hidden';
qu_captcha.canvas.width = qu_captcha.min_dimension * 0.9;
qu_captcha.canvas.height = qu_captcha.canvas.width

qu_captcha.loader = document.createElement('div');
qu_captcha.loader.className = 'qu-captcha-loading';

qu_captcha.containerInit = document.createElement('div');
qu_captcha.containerInit.className = 'qu-captcha-container qu-captcha-reset-style';

qu_captcha.robotP = document.createElement('p');
qu_captcha.robotP.className = 'qu-captcha-p';
qu_captcha.robotP.style.whiteSpace = 'nowrap';
qu_captcha.robotP.textContent = 'Вы — робот?';

qu_captcha.robotButton = document.createElement('button');
qu_captcha.robotButton.type = 'button';
qu_captcha.robotButton.className = 'qu-captcha-button';
qu_captcha.robotButton.textContent = 'Нет';
qu_captcha.containerInit.append(qu_captcha.robotP, qu_captcha.robotButton);

qu_captcha.inlineWrapper = document.createElement('div');
qu_captcha.inlineWrapper.style = 'display:flex;align-items:center;gap:15px;';
qu_captcha.inlineWrapper.append(qu_captcha.robotP, qu_captcha.robotButton);
qu_captcha.containerInit.appendChild(qu_captcha.inlineWrapper);

qu_captcha.buttonGroup = document.createElement('div');
qu_captcha.buttonGroup.className = 'qu-captcha-button-group';

qu_captcha.exampleButton = document.createElement('button');
qu_captcha.exampleButton.type = 'button';
qu_captcha.exampleButton.className = 'qu-captcha-gray-button';
qu_captcha.exampleButton.textContent = 'Пример';
qu_captcha.exampleButton.onclick = () => {
    window.open('https://telegra.ph/Instrukciya-QuCaptcha-04-13', '_blank');
    return false;
};

qu_captcha.resetButton = document.createElement('button');
qu_captcha.resetButton.type = 'button';
qu_captcha.resetButton.className = 'qu-captcha-gray-button';
qu_captcha.resetButton.textContent = 'Сброс';

qu_captcha.checkButton = document.createElement('button');
qu_captcha.checkButton.type = 'button';
qu_captcha.checkButton.className = 'qu-captcha-button';
qu_captcha.checkButton.textContent = 'Готово';

qu_captcha.retryButton = document.createElement('button');
qu_captcha.retryButton.type = 'button';
qu_captcha.retryButton.className = 'qu-captcha-button qu-captcha-hidden';
qu_captcha.retryButton.textContent = 'Заново';

qu_captcha.buttonGroup.append(qu_captcha.exampleButton, qu_captcha.resetButton, qu_captcha.checkButton, qu_captcha.retryButton);

qu_captcha.resultText = document.createElement('p');
qu_captcha.resultText.className = 'qu-captcha-p qu-captcha-hidden';

qu_captcha.hiddenInput = document.createElement('input');
qu_captcha.hiddenInput.type = 'hidden';
qu_captcha.hiddenInput.id = 'qu_captcha_human_token';
qu_captcha.hiddenInput.name = 'qu_captcha_human_token';

qu_captcha.container.append(
    qu_captcha.instruction,
    qu_captcha.resultText,
    qu_captcha.loader,
    qu_captcha.canvas,
    qu_captcha.buttonGroup,
);

qu_captcha.shadow.append(qu_captcha.containerInit);
qu_captcha.div.append(qu_captcha.hiddenInput);

qu_captcha.form.replaceWith(qu_captcha.div);

qu_captcha.ctx = qu_captcha.canvas.getContext('2d');

qu_captcha.isMobile = window.navigator.userAgent.toLowerCase().includes("mobile");
qu_captcha.img;
qu_captcha.task_id = '';

qu_captcha.user_dots = [];

function qu_captcha_disableForm(bool) {
    document.querySelectorAll('.qu-captcha-disable-item').forEach(item => {
        item.disabled = bool;
    });
    document.querySelectorAll('.qu-captcha-hide-item').forEach(item => {
        item.style.display = bool ? 'none' : 'block';
    });
    document.querySelectorAll('.qu-captcha-show-item').forEach(item => {
        item.style.display = bool ? 'block' : 'none';
    });
}

async function qu_captcha_loadCaptcha() {
    qu_captcha.canvas.classList.add('qu-captcha-hidden');
    qu_captcha.loader.style.display = 'block';
    const response = await fetch(qu_captcha.url + '/get_task?t=' + Date.now());
    const data = await response.json();
    qu_captcha.task_id = data.task_id;

    qu_captcha.img = new Image();
    qu_captcha.img.src = data.image;
    qu_captcha.img.onload = () => {
        qu_captcha.ctx.drawImage(qu_captcha.img, 0, 0, qu_captcha.canvas.width, qu_captcha.canvas.height);
        qu_captcha.loader.style.display = 'none';
        qu_captcha.canvas.classList.remove('qu-captcha-hidden');
    };
}

function qu_captcha_drawCircleWithNumber(x, y, number) {
    qu_captcha.ctx.beginPath();
    qu_captcha.ctx.arc(x, y, 10, 0, Math.PI * 2);
    qu_captcha.ctx.fillStyle = "red";
    qu_captcha.ctx.fill();
    qu_captcha.ctx.lineWidth = 1;
    qu_captcha.ctx.strokeStyle = "black";
    qu_captcha.ctx.stroke();
    qu_captcha.ctx.closePath();

    qu_captcha.ctx.fillStyle = "white";
    qu_captcha.ctx.font = "15px Arial";
    qu_captcha.ctx.textAlign = "center";
    qu_captcha.ctx.textBaseline = "middle";
    qu_captcha.ctx.fillText(number, x, y);
}

function qu_captcha_getXY(event) {
    const x = event.offsetX;
    const y = event.offsetY;

    const normalizedX = x / qu_captcha.canvas.width;
    const normalizedY = y / qu_captcha.canvas.height;
    return [x, y, normalizedX, normalizedY]
}

qu_captcha.canvas.addEventListener('click', (event) => {
    if (qu_captcha.resetButton.classList.contains('qu-captcha-hidden')) {return;}

    [x, y, normalizedX, normalizedY] = qu_captcha_getXY(event);

    qu_captcha.user_dots.push([normalizedX, normalizedY]);

    qu_captcha_drawCircleWithNumber(x, y, qu_captcha.user_dots.length)
});

function qu_captcha_reset() {
    qu_captcha.user_dots = [];
    qu_captcha.task_id = '';

    qu_captcha.ctx.clearRect(0, 0, qu_captcha.canvas.width, qu_captcha.canvas.height);
    qu_captcha.resultText.classList.add('qu-captcha-hidden');
    qu_captcha.retryButton.classList.add('qu-captcha-hidden');
    qu_captcha.instruction.classList.remove('qu-captcha-hidden');
    qu_captcha.canvas.classList.remove('qu-captcha-hidden');
    qu_captcha.exampleButton.classList.remove('qu-captcha-hidden');
    qu_captcha.resetButton.classList.remove('qu-captcha-hidden');
    qu_captcha.checkButton.classList.remove('qu-captcha-hidden');
}


qu_captcha.resetButton.addEventListener('click', async () => {
    if (qu_captcha.user_dots.length > 0) {
        let tmp = qu_captcha.task_id;
        qu_captcha_reset();
        qu_captcha.task_id = tmp;
        qu_captcha.ctx.drawImage(qu_captcha.img, 0, 0, qu_captcha.canvas.width, qu_captcha.canvas.height);
    }
});

qu_captcha.checkButton.addEventListener('click', async () => {
    if (qu_captcha.user_dots.length == 0) {
        alert("Не введено решение для капчи");
        return;
    }
    qu_captcha.canvas.classList.add('qu-captcha-hidden');
    qu_captcha.loader.style.display = 'block';

    task_id = qu_captcha.task_id;
    user_dots = qu_captcha.user_dots;
    const response = await fetch(qu_captcha.url + '/check_task', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ task_id, user_dots })
    });

    const result = await response.json();
    qu_captcha.instruction.classList.add('qu-captcha-hidden');
    qu_captcha.resetButton.classList.add('qu-captcha-hidden');
    qu_captcha.checkButton.classList.add('qu-captcha-hidden');

    if (result.solved) {
        qu_captcha.hiddenInput.value = result.human_token;
        qu_captcha_disableForm(false);
        qu_captcha.exampleButton.classList.add('qu-captcha-hidden');
        qu_captcha.resultText.innerHTML = '<span style="color: green;">&#10004;</span> Вы — человек';
        qu_captcha.container.removeAttribute('id');
        if (qu_captcha.uses_cookie) {
            document.cookie = `qu_captcha_human_token=${result.human_token};samesite=strict;max-age=3600`
        }
    } else {
        if (result.solution) {
            qu_captcha.canvas.classList.remove('qu-captcha-hidden');
            qu_captcha.resultText.textContent = 'Задача не решена. Верное решение:';
            qu_captcha.ctx.clearRect(0, 0, qu_captcha.canvas.width, qu_captcha.canvas.height);
            qu_captcha.ctx.drawImage(qu_captcha.img, 0, 0, qu_captcha.canvas.width, qu_captcha.canvas.height);
            for (let i = 0; i < result.solution.length; i++) {
                qu_captcha_drawCircleWithNumber(Math.floor(result.solution[i][0] * qu_captcha.canvas.width), Math.floor(result.solution[i][1] * qu_captcha.canvas.width), i+1);
            }
        } else {
            qu_captcha.resultText.textContent = 'Задача просрочена';
        }
        qu_captcha.retryButton.classList.remove('qu-captcha-hidden');
    }
    qu_captcha.resultText.classList.remove('qu-captcha-hidden');
    qu_captcha.loader.style.display = 'none';
    if (result.solved) { qu_captcha = {}; }
});

qu_captcha.retryButton.addEventListener('click', () => {
    qu_captcha_reset();
    qu_captcha_loadCaptcha();
});

qu_captcha.robotButton.addEventListener('click', () => {
    qu_captcha.containerInit.replaceWith(qu_captcha.container);
    qu_captcha_loadCaptcha();
});

qu_captcha_disableForm(true);
