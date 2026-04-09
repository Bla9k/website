<script>
	const dailyGoal = 2200;
	const waterGoalMl = 3000;

	const packagedFoodCatalog = {
		'012345678905': {
			name: 'Greek Yogurt Cup',
			brand: 'Natura',
			serving: '170 g',
			calories: 190,
			protein: 15,
			carbs: 16,
			fat: 8
		},
		'5901234123457': {
			name: 'Protein Oats',
			brand: 'FitHarvest',
			serving: '60 g',
			calories: 240,
			protein: 12,
			carbs: 39,
			fat: 5
		},
		'8111111111116': {
			name: 'Chicken Caesar Wrap',
			brand: 'Fresh Bite',
			serving: '1 wrap',
			calories: 430,
			protein: 28,
			carbs: 35,
			fat: 19
		}
	};

	const seededEntries = [
		{
			id: crypto.randomUUID(),
			source: 'barcode',
			code: '012345678905',
			time: '08:12',
			...packagedFoodCatalog['012345678905']
		},
		{
			id: crypto.randomUUID(),
			source: 'qr',
			code: '8111111111116',
			time: '13:08',
			...packagedFoodCatalog['8111111111116']
		}
	];

	let entries = seededEntries;
	let lastScanMessage = 'Ready to scan a barcode or nutrition QR.';
	let waterIntakeMl = 1850;

	const totals = () =>
		entries.reduce(
			(acc, item) => ({
				calories: acc.calories + item.calories,
				protein: acc.protein + item.protein,
				carbs: acc.carbs + item.carbs,
				fat: acc.fat + item.fat
			}),
			{ calories: 0, protein: 0, carbs: 0, fat: 0 }
		);

	$: nutritionTotals = totals();
	$: consumedPercent = Math.min(100, Math.round((nutritionTotals.calories / dailyGoal) * 100));
	$: waterPercent = Math.min(100, Math.round((waterIntakeMl / waterGoalMl) * 100));

	function handleScan(code, source) {
		const data = packagedFoodCatalog[code];

		if (!data) {
			lastScanMessage = `No verified nutrition profile found for ${code}.`; 
			return;
		}

		entries = [
			{
				id: crypto.randomUUID(),
				source,
				code,
				time: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
				...data
			},
			...entries
		];
		lastScanMessage = `${data.name} added from ${source.toUpperCase()} (${code}).`;
	}

	function addWater(amount) {
		waterIntakeMl = Math.min(waterGoalMl, waterIntakeMl + amount);
	}
</script>

<svelte:head>
	<title>NutriLens — Mobile Calorie Tracker</title>
	<meta
		name="description"
		content="NutriLens mobile calorie tracker with barcode + nutrition QR scanning and macro tracking dashboard."
	/>
</svelte:head>

<div class="app-shell">
	<header class="hero">
		<p class="badge">NutriLens</p>
		<h1>Track calories accurately from barcode + nutrition QR scans.</h1>
		<p>
			Built for packaged foods, with per-serving nutrition parsing and real-time macro totals in a premium,
			mobile-first UI.
		</p>
	</header>

	<section class="card progress-card">
		<div>
			<p class="label">Daily calories</p>
			<p class="value">{nutritionTotals.calories} / {dailyGoal} kcal</p>
		</div>
		<div class="meter" role="progressbar" aria-valuenow={consumedPercent} aria-valuemin="0" aria-valuemax="100">
			<span style={`width:${consumedPercent}%`}></span>
		</div>
		<p class="tiny">{consumedPercent}% of target consumed</p>
	</section>

	<section class="card scan-card">
		<div class="scan-header">
			<h2>Instant Nutrition Scan</h2>
			<p>{lastScanMessage}</p>
		</div>
		<div class="scan-actions">
			<button on:click={() => handleScan('5901234123457', 'barcode')}>Scan Barcode</button>
			<button class="secondary" on:click={() => handleScan('8111111111116', 'qr')}>Scan Nutrition QR</button>
		</div>
	</section>

	<section class="card macros-card">
		<h3>Macro split</h3>
		<div class="macros">
			<article>
				<p>Protein</p>
				<strong>{nutritionTotals.protein}g</strong>
			</article>
			<article>
				<p>Carbs</p>
				<strong>{nutritionTotals.carbs}g</strong>
			</article>
			<article>
				<p>Fat</p>
				<strong>{nutritionTotals.fat}g</strong>
			</article>
		</div>
	</section>

	<section class="card hydration-card">
		<div>
			<h3>Hydration</h3>
			<p>{waterIntakeMl} / {waterGoalMl} ml</p>
		</div>
		<div class="meter compact"><span style={`width:${waterPercent}%`}></span></div>
		<div class="chips">
			<button on:click={() => addWater(250)}>+250 ml</button>
			<button on:click={() => addWater(500)}>+500 ml</button>
		</div>
	</section>

	<section class="card logs-card">
		<div class="logs-head">
			<h3>Today’s meals</h3>
			<p>{entries.length} entries</p>
		</div>
		<ul>
			{#each entries as entry}
				<li>
					<div>
						<p class="food">{entry.name}</p>
						<p class="meta">{entry.brand} • {entry.serving} • {entry.time}</p>
					</div>
					<div class="kcal">{entry.calories} kcal</div>
				</li>
			{/each}
		</ul>
	</section>
</div>

<style>
	:global(body) {
		margin: 0;
		font-family: Inter, SF Pro Display, system-ui, -apple-system, sans-serif;
		background: radial-gradient(circle at 15% 10%, #1f3b6e 0%, #090e1a 40%, #05070f 100%);
		color: #f9fbff;
	}

	.app-shell {
		max-width: 430px;
		margin: 0 auto;
		padding: 1.2rem 1rem 2.5rem;
		display: grid;
		gap: 0.9rem;
	}

	.hero {
		padding: 0.65rem 0.2rem 0.3rem;
	}

	.hero h1 {
		font-size: clamp(1.45rem, 6vw, 2rem);
		line-height: 1.15;
		margin: 0.5rem 0 0.65rem;
	}

	.hero p {
		margin: 0;
		color: #c6d2eb;
		line-height: 1.4;
	}

	.badge {
		display: inline-block;
		font-weight: 600;
		padding: 0.35rem 0.65rem;
		border-radius: 999px;
		background: linear-gradient(110deg, #1fe3ae, #4ac4ff);
		color: #041123;
		font-size: 0.78rem;
	}

	.card {
		border: 1px solid rgba(141, 188, 255, 0.22);
		background: linear-gradient(165deg, rgba(16, 27, 49, 0.93), rgba(7, 12, 24, 0.96));
		backdrop-filter: blur(12px);
		border-radius: 20px;
		padding: 1rem;
		box-shadow: 0 14px 30px rgba(0, 0, 0, 0.35);
	}

	.label,
	.tiny,
	.scan-header p,
	.logs-head p,
	.meta,
	.hydration-card p {
		margin: 0;
		font-size: 0.84rem;
		color: #afbedb;
	}

	.value {
		font-size: 1.1rem;
		margin: 0.2rem 0 0.7rem;
		font-weight: 700;
	}

	.meter {
		height: 11px;
		background: rgba(255, 255, 255, 0.08);
		border-radius: 999px;
		overflow: hidden;
		margin-bottom: 0.45rem;
	}

	.meter span {
		display: block;
		height: 100%;
		background: linear-gradient(90deg, #53e8ba, #6bc4ff);
	}

	.scan-header h2,
	.macros-card h3,
	.hydration-card h3,
	.logs-head h3 {
		margin: 0;
	}

	.scan-header {
		margin-bottom: 0.7rem;
	}

	.scan-actions {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 0.5rem;
	}

	button {
		font: inherit;
		border: none;
		padding: 0.7rem;
		border-radius: 12px;
		font-weight: 600;
		cursor: pointer;
		background: linear-gradient(95deg, #61f0c2, #73b8ff);
		color: #061121;
	}

	button.secondary {
		background: rgba(137, 169, 226, 0.15);
		color: #d8e6ff;
		border: 1px solid rgba(145, 187, 255, 0.4);
	}

	.macros {
		display: grid;
		grid-template-columns: repeat(3, 1fr);
		gap: 0.55rem;
		margin-top: 0.7rem;
	}

	.macros article {
		background: rgba(129, 164, 230, 0.12);
		padding: 0.7rem;
		border-radius: 12px;
	}

	.macros p {
		margin: 0;
		font-size: 0.76rem;
		color: #bad0f3;
	}

	.macros strong {
		font-size: 1rem;
	}

	.hydration-card {
		display: grid;
		gap: 0.65rem;
	}

	.meter.compact {
		margin: 0;
	}

	.chips {
		display: flex;
		gap: 0.45rem;
	}

	.chips button {
		flex: 1;
		background: rgba(101, 143, 218, 0.22);
		color: #e5efff;
		border: 1px solid rgba(145, 187, 255, 0.35);
	}

	.logs-head {
		display: flex;
		align-items: baseline;
		justify-content: space-between;
		margin-bottom: 0.6rem;
	}

	ul {
		list-style: none;
		padding: 0;
		margin: 0;
		display: grid;
		gap: 0.55rem;
	}

	li {
		display: flex;
		justify-content: space-between;
		gap: 0.5rem;
		background: rgba(96, 132, 196, 0.14);
		padding: 0.7rem;
		border-radius: 12px;
	}

	.food {
		margin: 0;
		font-weight: 600;
	}

	.kcal {
		font-weight: 700;
		color: #b7f5de;
		white-space: nowrap;
	}
</style>
