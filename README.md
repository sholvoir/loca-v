# LocaV

LocaV is a visualization tool of ancestral data.
Which accept ancesstral analysis result data file (csv/tsv format) as input and draws images of samples.
The images use colors to present the ancestral soure of the gene snippet.

## Usage

1. Please sure the **JRE 8** be installed well.
2. Download the software from http://4dgenome.com/download/locav.zip and extract it to a folder.
3. The executable scripts are in the "bin" folder, you can add this directory to your PATH or use full path to use the program.
4. Run the software with the following command:
    ```bash
    [path/]plotp|plotc [option]
    ```
    plotp use for ploting whole genome image of sigle person.  
    plotc use for ploting a single chromosome of multi people for comparing.
5. Use followinng command to get help:
    ```bash
    [path]plotp|plotc --help
    ```

## Input Data Format

LocaV requires a group of csv/tsv with header format input files which contain ancestral analysis data for each chromosome: chr1.loca, chr2.loca ... chr22.loca, chrX.loca, chrY.loca.

Every .loca file must include a position column which indicate the postion of loci of a SNP in chromsome and several SAMPLEID_A and SAMPLEID_B colomns whose value should be a single character which indicate where the sample's SNP at this loci come from. The input filename is prefer *chrX.loca* like above list otherwise you need extra config in command line.

Here is an example file (chr1.loca):

```tsv
rsID position_b36	NA12749_A	NA12749_B	NA12748_A	NA12748_B	NA12890_A	NA12890_B
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

## Outputs

plotp will output the file: NA12749.png  
plotc will output the file: chr1.png