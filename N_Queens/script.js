/* Backtracking solver that returns array of solutions.
   Each solution is an array `cols` where cols[row] = column index of queen in that row.
*/
function solveNQueensAll(n){
  const solutions = [];
  const cols = new Array(n).fill(false);
  const diag1 = new Array(2*n).fill(false); // row+col
  const diag2 = new Array(2*n).fill(false); // row-col+n
  const boardCols = new Array(n).fill(-1);

  function backtrack(row){
    if(row === n){
      solutions.push(boardCols.slice());
      return;
    }
    for(let c=0;c<n;c++){
      if(cols[c] || diag1[row+c] || diag2[row-c+n]) continue;
      cols[c] = diag1[row+c] = diag2[row-c+n] = true;
      boardCols[row] = c;
      backtrack(row+1);
      cols[c] = diag1[row+c] = diag2[row-c+n] = false;
      boardCols[row] = -1;
    }
  }

  backtrack(0);
  return solutions;
}

/* Render a given solution (cols array) as chessboard in #boardContainer */
function renderBoard(cols){
  const n = cols.length;
  const container = document.getElementById('boardContainer');
  container.innerHTML = '';
  // adapt board size variable for visual scale by number of cells
  const base = Math.min(540, Math.max(240, n * 60));
  document.documentElement.style.setProperty('--board-size', base + 'px');

  container.style.gridTemplateColumns = `repeat(${n}, 1fr)`;
  container.style.gridTemplateRows = `repeat(${n}, 1fr)`;

  for(let r=0;r<n;r++){
    for(let c=0;c<n;c++){
      const cell = document.createElement('div');
      cell.className = 'cell';
      const isDark = (r + c) % 2 === 1;
      cell.style.background = isDark ? getComputedStyle(document.documentElement).getPropertyValue('--dark') : getComputedStyle(document.documentElement).getPropertyValue('--light');
      if(cols[r] === c){
        const q = document.createElement('div');
        q.className = 'queen';
        q.innerHTML = '♕';
        cell.appendChild(q);
      }
      container.appendChild(cell);
    }
  }
}

/* UI logic */
let solutions = [];
let currentIndex = 0;
let autoplayInterval = null;

const nInput = document.getElementById('nInput');
const generateBtn = document.getElementById('generateBtn');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');
const autoBtn = document.getElementById('autoBtn');
const status = document.getElementById('status');
const solInfo = document.getElementById('solutionInfo');

generateBtn.addEventListener('click', () => {
  const n = parseInt(nInput.value, 10);
  if(isNaN(n) || n < 1) { alert('Please enter a positive integer for N.'); return; }
  status.textContent = `Solving for N = ${n} ...`;
  // Slight delay to show status before heavy computation
  setTimeout(() => {
    solutions = solveNQueensAll(n);
    currentIndex = 0;
    if(solutions.length === 0){
      status.textContent = `No solutions for N = ${n}.`;
      renderEmpty(n);
      updateButtons();
      solInfo.textContent = '';
    } else {
      status.textContent = `Found ${solutions.length} solution${solutions.length>1?'s':''} for N = ${n}.`;
      renderBoard(solutions[currentIndex]);
      updateSolutionInfo();
      updateButtons();
    }
  }, 30);
});

prevBtn.addEventListener('click', () => {
  if(solutions.length === 0) return;
  currentIndex = (currentIndex - 1 + solutions.length) % solutions.length;
  renderBoard(solutions[currentIndex]);
  updateSolutionInfo();
});

nextBtn.addEventListener('click', () => {
  if(solutions.length === 0) return;
  currentIndex = (currentIndex + 1) % solutions.length;
  renderBoard(solutions[currentIndex]);
  updateSolutionInfo();
});

autoBtn.addEventListener('click', () => {
  if(autoplayInterval){
    clearInterval(autoplayInterval);
    autoplayInterval = null;
    autoBtn.textContent = 'Auto Play';
    prevBtn.disabled = nextBtn.disabled = false;
  } else {
    if(solutions.length === 0) return;
    autoplayInterval = setInterval(() => {
      nextBtn.click();
    }, 900);
    autoBtn.textContent = 'Stop';
    prevBtn.disabled = nextBtn.disabled = true;
  }
});

function updateButtons(){
  const has = solutions.length > 0;
  prevBtn.disabled = !has;
  nextBtn.disabled = !has;
  autoBtn.disabled = !has;
}

function updateSolutionInfo(){
  solInfo.textContent = `Solution ${currentIndex + 1} / ${solutions.length}`;
  status.textContent = `Showing solution ${currentIndex + 1} of ${solutions.length}. (N = ${solutions[0].length})`;
}

function renderEmpty(n){
  const container = document.getElementById('boardContainer');
  container.innerHTML = '';
  container.style.gridTemplateColumns = `repeat(${n}, 1fr)`;
  container.style.gridTemplateRows = `repeat(${n}, 1fr)`;
  for(let r=0;r<n;r++){
    for(let c=0;c<n;c++){
      const cell = document.createElement('div');
      cell.className = 'cell';
      const isDark = (r + c) % 2 === 1;
      cell.style.background = isDark ? getComputedStyle(document.documentElement).getPropertyValue('--dark') : getComputedStyle(document.documentElement).getPropertyValue('--light');
      container.appendChild(cell);
    }
  }
}
