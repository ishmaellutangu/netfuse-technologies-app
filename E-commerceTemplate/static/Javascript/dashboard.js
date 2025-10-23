document.addEventListener('DOMContentLoaded', function () {
	const profileBtn = document.querySelector('.profile-btn');
	const dropdown = document.getElementById('profileDropdown');

	if (!profileBtn || !dropdown) return;

	function openDropdown() {
		dropdown.classList.add('open');
		dropdown.setAttribute('aria-hidden', 'false');
		profileBtn.setAttribute('aria-expanded', 'true');
	}

	function closeDropdown() {
		dropdown.classList.remove('open');
		dropdown.setAttribute('aria-hidden', 'true');
		profileBtn.setAttribute('aria-expanded', 'false');
	}

	profileBtn.addEventListener('click', function (e) {
		e.stopPropagation();
		if (dropdown.classList.contains('open')) {
			closeDropdown();
		} else {
			openDropdown();
		}
	});

	// Close when clicking outside
	document.addEventListener('click', function (e) {
		if (!dropdown.contains(e.target) && !profileBtn.contains(e.target)) {
			closeDropdown();
		}
	});

	// Close on Escape
	document.addEventListener('keydown', function (e) {
		if (e.key === 'Escape') {
			closeDropdown();
		}
	});
});
