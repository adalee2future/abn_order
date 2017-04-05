#!/bin/ksh -eu

# generate report using R
R --no-save << EOT
rmarkdown::render('abn_order_daily2.Rmd',
                  output_format='html_document',
		  output_file='abn_ord_dly.$rpt_date.html',
		  params=list(rpt_date="$rpt_date")
)

rmarkdown::render('abn_ord_dly_app.Rmd',
                  output_format='html_document',
		  output_file='abn_ord_dly_app.$rpt_date.html',
		  params=list(rpt_date="$rpt_date")
)

rmarkdown::render('abn_ord_dly_smy.Rmd',
                  output_format='html_document',
		  output_file='abn_ord_dly_smy.$rpt_date.html',
		  params=list(rpt_date="$rpt_date")
)

rmarkdown::render('index.Rmd',
                  output_format='html_document',
		  params=list(rpt_date="$rpt_date")
)

EOT

mv abn_ord_dly*.$rpt_date.html output/
cp index.html output/

