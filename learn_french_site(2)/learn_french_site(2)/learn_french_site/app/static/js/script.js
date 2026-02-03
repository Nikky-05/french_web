/* small interactions for vocab cards, audio play and quizzes */
(function(){
  // Play audio if provided
  document.addEventListener('click', function(e){
    if (e.target && e.target.matches('.play-sound')){
      const src = e.target.dataset.audio;
      if (!src) return;
      const a = new Audio(src);
      a.play();
    }
  });

  // Quizzes: simple selection + submit
  function initQuizzes(){
    const quizzes = document.querySelectorAll('.quiz');
    quizzes.forEach(q => {
      q.querySelectorAll('.option').forEach(btn => {
        btn.addEventListener('click', function(){
          // mark selected
          const parent = this.closest('.mcq');
          parent.querySelectorAll('.option').forEach(b=>b.classList.remove('selected'));
          this.classList.add('selected');
        });
      });

      const submit = q.querySelector('.submit-quiz');
      const start = q.querySelector('.start-quiz');
      const resultEl = q.querySelector('.quiz-result');

      if (start) start.addEventListener('click', () => {
        q.scrollIntoView({behavior:'smooth', block:'center'});
      });

      if (submit) submit.addEventListener('click', () => {
        const items = q.querySelectorAll('.mcq');
        let total = items.length, correct = 0;
        items.forEach(item => {
          const ans = item.dataset.answer;
          const sel = item.querySelector('.option.selected');
          if (sel && sel.textContent.trim() === ans.trim()){
            correct++;
            item.style.borderLeft = "4px solid #34d399"; // green
          } else {
            item.style.borderLeft = "4px solid #ff7b7b"; // red
          }
        });
        resultEl.textContent = `Score: ${correct} / ${total}`;
      });
    });
  }

  window.initQuizzes = initQuizzes;
  document.addEventListener('DOMContentLoaded', initQuizzes);
})();
