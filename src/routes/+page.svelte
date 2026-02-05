<svelte:head>
	<title>Simple Website</title>
	<meta name="description" content="A simple Svelte website with a hero, features, and contact section." />
</svelte:head>

<div class="page">
	<header class="hero">
		<p class="badge">Welcome</p>
		<h1>Simple Website</h1>
		<p>
			This is a clean starter page built with Svelte. You can use it as a base for your own
			portfolio, landing page, or product site.
		</p>
		<a href="#contact">Get in touch</a>
	</header>

	<section class="section">
		<h2>What this includes</h2>
		<div class="grid">
			<article class="card">
				<h3>Responsive Layout</h3>
				<p>Looks good on mobile, tablet, and desktop screens.</p>
			</article>
			<article class="card">
				<h3>Simple Styling</h3>
				<p>Minimal custom CSS with clear spacing and typography.</p>
			</article>
			<article class="card">
				<h3>Easy to Extend</h3>
				<p>Add sections for projects, testimonials, or a blog in minutes.</p>
			</article>
		</div>
	</section>

	<section class="section contact" id="contact">
		<h2>Contact</h2>
		<p>Email: hello@example.com</p>
	</section>
</div>

<style>
	.page {
		max-width: 960px;
		margin: 0 auto;
		padding: 2rem 1rem 4rem;
		font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, sans-serif;
		color: #1f2937;
	}

	.hero {
		text-align: center;
		padding: 5rem 1rem 3rem;
	}

	.badge {
		display: inline-block;
		padding: 0.35rem 0.75rem;
		border-radius: 999px;
		background: #e0e7ff;
		color: #3730a3;
		font-weight: 600;
		font-size: 0.875rem;
		margin-bottom: 1rem;
	}

	h1 {
		font-size: clamp(2rem, 6vw, 3.4rem);
		margin-bottom: 1rem;
	}

	.hero p {
		max-width: 640px;
		margin: 0 auto 1.5rem;
		line-height: 1.65;
	}

	a {
		display: inline-block;
		text-decoration: none;
		background: #111827;
		color: #ffffff;
		padding: 0.75rem 1.25rem;
		border-radius: 0.5rem;
		font-weight: 600;
	}

	.section {
		margin-top: 3rem;
	}

	h2 {
		font-size: 1.6rem;
		margin-bottom: 1rem;
	}

	.grid {
		display: grid;
		grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
		gap: 1rem;
	}

	.card {
		border: 1px solid #e5e7eb;
		border-radius: 0.75rem;
		padding: 1rem;
		background: #ffffff;
		box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06);
	}

	.card h3 {
		margin-bottom: 0.5rem;
	}

	.contact {
		padding: 1.25rem;
		border-radius: 0.75rem;
		background: #f9fafb;
	}
</style>
