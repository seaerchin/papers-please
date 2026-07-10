---
id: vitest
aliases: []
tags: []
---
- a few ways to do browser testing
	- simulate the DOM (`jsdom`) does this
	- test against a real browser (`cypress`)
	- provide a browser engine (`playwright`)

# dom simulation
- might have short-comings because real browser engines might not match up w/ the simulation
# browser compat
- vitest uses `Vite dev server` to run your tests, so only features specified w/ `esbuild.target`
- vite targets browsers which support ESM modules, dynamic import, `import.meta`
	- also use `BroadcastChannel` to communicate b/w iframes 
# running tests 
- vitest will try to run specified browser using `preview` but we can also use `headless` mode 
	- `preview` opens the browser; `headless` doesn't 
# limitations
## thread blocking dialogs
- `alerts` or `dialog` or `confirm` cannot be used cos it stops browser communication w/ vitest 
- vitest provides **default mocks** with **default returned values** -> we should mock the values ourselves
## spying on module exports
- browser mode uses browser's native ESM support to serve modules
- the `module` namespace object is sealed -> cannot be reconfigured
	- we cannot call `vi.spyOn`on an imported object