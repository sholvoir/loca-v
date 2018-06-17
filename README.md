# LocaV

LocaV is a visualization tool of ancestral analytics result data.
Which accept ancesstral analytics result data file (csv/tsv format) as input and draws images of each sample.
The images use colors to present the ancestral soure of the gene snippet.

## Usage

1. Please make sure the **JRE 8 or above** be installed well.
2. Download the software from http://4dgenome.com/download/locav.zip and extract it to a folder.
3. The executable scripts are in the "bin" folder, you can add this directory to your PATH or use full path to run it.
4. Run the software with the following command:
    ```bash
    [path/]plotp|plotc [options]
    ```
    "plotp" is used to plot whole genome image of sigle person.
    "plotc" is used to ploting a single chromosome of multi people for comparing.
5. If you want to get more information of *options* of the command line, use followinng command to get help:
    ```bash
    [path]plotp|plotc --help
    ```

## Input Data Format

LocaV requires a group of csv/tsv format files as input which contain ancestral analytics result data for each chromosome, such as chr1.loca, chr2.loca ... chr22.loca, chrX.loca, chrY.loca.

Each .loca file must include a position column which indicate the postion of loci of a SNP in chromsome and several SAMPLEID_A and SAMPLEID_B colomns which indicate where the sample's SNP come from and the value of the columns should be a single character. The name of input file prefer *chrX.loca* like above list otherwise you need extra config in command line.

Here is an example file (chr1.loca):

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

## Outputs

"plotp" command will output the file: NA12749.png, NA12748.png and NA12890.png.  
"plotc" command will output the file: chr1.png.