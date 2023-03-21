# nvim-jdtls-bundles

Forked from [nvim-jdtls-bundles](https://gitlab.com/schrieveslaach/nvim-jdtls-bundles)
---

Helper plugin to load [eclipse.jdt.ls][1] extensions from the VSCode marketplace to make the setup of [nvim-jdtls][2] more convinient.

# Usage

Install [nvim-jdtls][2], [nvim-dap][6], [plenary.nvim](https://github.com/nvim-lua/plenary.nvim), and [nvim-jdtls-bundles](https://gitlab.com/schrieveslaach/nvim-jdtls-bundles) through your Neovim plugin manager. The following code shows the install with [vim-plug](https://github.com/junegunn/vim-plug):

```viml
Plug 'mfussenegger/nvim-jdtls'
Plug 'mfussenegger/nvim-dap'
Plug 'nvim-lua/plenary.nvim'
Plug 'https://gitlab.com/schrieveslaach/nvim-jdtls-bundles', { 'do': './install-bundles.py' }
```

The example with vim-plug uses the [post-update hook](https://github.com/junegunn/vim-plug#post-update-hooks) to run the script `install-bundles.py` to download and extract the VSCode bundles. By default the script installs [VSCode Debugger for Java][3] and [VSCode Test Runner for Java][4]. See the scripts help for more information (run `./install-bundles.py -h`). For example, the option `--pde` installs [VSCode Eclipse PDE Support][5].

Finally, you can use `nvim-jdtls-bundles`' API to extend the `nvim-jdtls` configuration:

```lua
local config = {
   cmd = {
      -- …
   },

  init_options = {
    bundles = require('nvim-jdtls-bundles').bundles()
  },
}

require('jdtls').start_or_attach(config)
```

This example sets up [eclipse.jdt.ls][1] and [nvim-jdtls][2] so that you can use debugging and test running out of the box (you do not need to install the extension manually on your machine).

[1]: https://github.com/eclipse/eclipse.jdt.ls
[2]: https://github.com/mfussenegger/nvim-jdtls
[3]: https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug
[4]: https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-test
[5]: https://marketplace.visualstudio.com/items?itemName=yaozheng.vscode-pde
[6]: https://github.com/mfussenegger/nvim-dap

