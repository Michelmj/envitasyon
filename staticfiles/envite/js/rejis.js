
function copyValue(btn, value) {
      navigator.clipboard.writeText(value).then(() => {
        btn.textContent = '✓ Copied';
        btn.classList.add('copied');
        setTimeout(() => {
          btn.textContent = 'Copy';
          btn.classList.remove('copied');
        }, 2500);
      });
    }

    