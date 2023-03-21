local M = {}

M.bundles = function()
   local Path = require('plenary.path')
   local plugin_directory = Path:new(debug.getinfo(1).source:match("@?(.*/)")):parent()
   local bundles_path = plugin_directory:joinpath('bundles')

   local bundles = {}

   local scan = require('plenary.scandir')
   scan.scan_dir(bundles_path.filename, {
      hidden = true,
      depth = 2,
      on_insert = function(file)
         vim.list_extend(bundles, { file })
      end
   })

   return bundles
end

return M
