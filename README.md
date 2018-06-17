# LocaV

LocaV is a visualization software of ancestral data tool.
Which accept ancesstral analysis result data file (csv/tsv format) as input and draws images of samples.

## Runing Everionment

* jre 8

## Usage

1. Download this program from http://4dgenome.com/download/locav.zip.
2. Extract to a folder.
3. The executable script in the "bin" folder, you can add this directory to your PATH or use full path to use the program.
4. Run the software with the following command: [path/]plotp|plotc [option].
5. Use command plotp|plotc --help to get help.

## Input Data Format

LocaV requires a group of csv/tsv format with header input files which contain ancestral analysis data for each chromosome
chr1.loca, chr2.loca ... chr22.loca, chrX.loca, chrY.loca.

Every .loca file must include a position colomn which indicate the postion of loci of a SNP in chromsome and several SAMPLEID_A and SAMPLEID_B colomns whose value should be a single character which indicate where this sample at this loci come from. The file name is prefer the name above otherwise you need extra config in command line.

Here is an Example:

```tsv
rsID	position_b36	NA12749_A	NA12749_B	NA12748_A	NA12748_B	NA12890_A	NA12890_B
rs10458597	554484	0	0	2	0	2	0
rs2185539	556738	0	0	2	0	2	0
rs11240767	718814	0	0	2	0	2	0
rs12564807	724325	0	0	2	0	2	0
rs3131972	742584	0	0	2	0	2	0
rs3131969	744045	0	0	2	0	2	0
rs3131967	744197	0	0	2	0	2	0
rs1048488	750775	0	0	2	0	2	0
rs12562034	758311	0	0	2	0	2	0
rs12124819	766409	0	0	2	0	2	0
rs4040617	769185	0	0	2	0	2	0
rs2905036	782343	0	0	2	0	2	0
```