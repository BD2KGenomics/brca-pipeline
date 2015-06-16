# LOVD2 Test Pages
NMDB2_HOMEPAGE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>Switch gene - Leiden Muscular Dystrophy pages - Leiden Open Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
  <META name="Author" content="LOVD development team, LUMC, Netherlands">
  <META name="Generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <LINK rel="stylesheet" type="text/css" href="./styles.css">
  <LINK rel="shortcut icon" href="./favicon.ico">
  <LINK rel="alternate" type="application/atom+xml" title="Leiden Muscular Dystrophy pages Atom 1.0 feed" href="./api/feed.php" />

  <SCRIPT type="text/javascript">
    <!--
    navHome_B     = new Image();
    navHome_B.src = './gfx/tab_home_B.png';
    navHome_H     = new Image();
    navHome_H.src = './gfx/tab_home_H.png';
    navVariants_B     = new Image();
    navVariants_B.src = './gfx/tab_variants_B.png';
    navVariants_H     = new Image();
    navVariants_H.src = './gfx/tab_variants_H.png';
    navSubmitters_B     = new Image();
    navSubmitters_B.src = './gfx/tab_submitters_B.png';
    navSubmitters_H     = new Image();
    navSubmitters_H.src = './gfx/tab_submitters_H.png';
    navSubmit_B     = new Image();
    navSubmit_B.src = './gfx/tab_submit_B.png';
    navSubmit_H     = new Image();
    navSubmit_H.src = './gfx/tab_submit_H.png';
    navDocs_B     = new Image();
    navDocs_B.src = './gfx/tab_docs_B.png';
    navDocs_H     = new Image();
    navDocs_H.src = './gfx/tab_docs_H.png';

    // Used for tab images.
    function lovd_imageSwitch (image_id, image_mode) {
      document.getElementById(image_id).src = eval(image_id + '_' + image_mode + '.src');
    }

    function lovd_switchGeneInline () {
      varForm = '<FORM action="/nmdb2/home.php" id="SelectGeneDBInline" method="get" style="margin : 0px;"><SELECT name="select_db" onchange="document.getElementById(\'SelectGeneDBInline\').submit();"><OPTION value="ACTA1">ACTA1 (ACTin, Alpha 1 (skeletal muscle))</OPTION><OPTION value="ACTC1">ACTC1 (Actin, alpha, cardiac muscle 1)</OPTION><OPTION value="AGRN">AGRN (Agrin)</OPTION><OPTION value="ANKRD1">ANKRD1 (Ankyrin repeat domain 1 (cardiac muscle))</OPTION><OPTION value="ANO5">ANO5 (Anoctamin 5)</OPTION><OPTION value="ARHGEF10">ARHGEF10 (Rho guanine nucleotide exchange factor (GEF) 10)</OPTION><OPTION value="ASAH1">ASAH1 (N-acylsphingosine amidohydrolase (acid ceramidase) 1)</OPTION><OPTION value="ATL1">ATL1 (Atlastin GTPase 1)</OPTION><OPTION value="B3GALNT2">B3GALNT2 (Beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION><OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION><OPTION value="BAG3">BAG3 (BCL2-associated athanogene 3)</OPTION><OPTION value="BANF1">BANF1 (Barrier to autointegration factor 1)</OPTION><OPTION value="BIN1">BIN1 (Bridging INtegrator 1)</OPTION><OPTION value="BSCL2">BSCL2 (Berardinelli-Seip congenital lipodystrophy 2 (seipin))</OPTION><OPTION value="CAPN3">CAPN3 (Calpain-3)</OPTION><OPTION value="CAV3">CAV3 (Caveolin-3)</OPTION><OPTION value="CCDC78">CCDC78 (Coiled-coil domain containing 78)</OPTION><OPTION value="CCT5">CCT5 (Chaperonin containing TCP1, subunit 5 (epsilon))</OPTION><OPTION value="CFL2">CFL2 (Cofilin 2)</OPTION><OPTION value="CHAT">CHAT (Choline O-acetyltransferase)</OPTION><OPTION value="CHKB">CHKB (Choline kinase beta)</OPTION><OPTION value="CHRNA1">CHRNA1 (cholinergic receptor, nicotinic, alpha 1 (muscle))</OPTION><OPTION value="CHRNB1">CHRNB1 (Cholinergic receptor, nicotinic, beta 1 (muscle))</OPTION><OPTION value="CHRND">CHRND (Cholinergic receptor, nicotinic, delta)</OPTION><OPTION value="CHRNE">CHRNE (Cholinergic receptor, nicotinic, epsilon)</OPTION><OPTION value="CNTN1">CNTN1 (Contactin 1)</OPTION><OPTION value="COL6A1">COL6A1 (Collagen type VI alpha 1)</OPTION><OPTION value="COL6A2">COL6A2 (Collagen type VI alpha 2)</OPTION><OPTION value="COL6A3">COL6A3 (Collagen type VI alpha 3)</OPTION><OPTION value="COLQ">COLQ (Collagen-like tail subunit (single strand of homotrimer) of asymme...))</OPTION><OPTION value="CRYAB">CRYAB (Crystallin, alpha-B)</OPTION><OPTION value="CTDP1">CTDP1 (CTD (carboxy-terminal domain, RNA polymerase II, polypeptide A) p...))</OPTION><OPTION value="DAG1">DAG1 (Dystrophin-Associated Glycoprotein 1)</OPTION><OPTION value="DCTN1">DCTN1 (dynactin 1)</OPTION><OPTION value="DES">DES (Desmin)</OPTION><OPTION value="DMD">DMD (Duchenne Muscular Dystrophy)</OPTION><OPTION value="DMD_d">DMD_d (Duchenne Muscular Dystrophy (whole exon changes))</OPTION><OPTION value="DNAJB6">DNAJB6 (DnaJ (Hsp40) homolog, subfamily B, member 6)</OPTION><OPTION value="DNM2">DNM2 (Dynamin 2)</OPTION><OPTION value="DOK7">DOK7 (Docking protein 7)</OPTION><OPTION value="DPM3">DPM3 (Dolichyl-Phosphate Mannosyltransferase polypeptide 3)</OPTION><OPTION value="DTNA">DTNA (Dystrobrevin alpha)</OPTION><OPTION value="DUX4">DUX4 (Double homeobox 4)</OPTION><OPTION value="DYSF">DYSF (Dysferlin)</OPTION><OPTION value="EGR2">EGR2 (early growth response 2)</OPTION><OPTION value="EMD">EMD (Emery-Dreifuss muscular dystrophy (emerin))</OPTION><OPTION value="FAM134B">FAM134B (family with sequence similarity 134, member B)</OPTION><OPTION value="FGD4">FGD4 (FYVE, RhoGEF and PH domain containing 4)</OPTION><OPTION value="FHL1">FHL1 (Four and a Half LIM domains 1)</OPTION><OPTION value="FIG4">FIG4 (FIG4 homolog, SAC1 lipid phosphatase domain containing (S. cerevis...))</OPTION><OPTION value="FKRP">FKRP (Fukutin-Related Protein)</OPTION><OPTION value="FKTN">FKTN (Fukutin)</OPTION><OPTION value="FLNC">FLNC (Filamin C)</OPTION><OPTION value="GAN">GAN (Gigaxonin)</OPTION><OPTION value="GARS">GARS (glycyl-tRNA synthetase)</OPTION><OPTION value="GDAP1">GDAP1 (ganglioside induced differentiation associated protein 1)</OPTION><OPTION value="GFPT1">GFPT1 (Glutamine-fructose-6-phosphate transaminase 1)</OPTION><OPTION value="GJB1">GJB1 (gap junction protein, beta 1, 32kDa)</OPTION><OPTION value="GK">GK (Glycerol Kinase)</OPTION><OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION><OPTION value="GNB4">GNB4 (Guanine nucleotide binding protein (G protein), beta polypeptide 4)</OPTION><OPTION value="GNE">GNE (glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase)</OPTION><OPTION value="GTDC2">GTDC2 (Glycosyltransferase-like domain containing 2)</OPTION><OPTION value="HSPB1">HSPB1 (heat shock 27kDa protein 1)</OPTION><OPTION value="HSPB3">HSPB3 (heat shock 27kDa protein 3)</OPTION><OPTION value="HSPB8">HSPB8 (heat shock 22kDa protein 8)</OPTION><OPTION value="IGHMBP2">IGHMBP2 (Immunoglobulin mu binding protein 2)</OPTION><OPTION value="IKBKAP">IKBKAP (inhibitor of kappa light polypeptide gene enhancer in B-cells, k...)</OPTION><OPTION value="ISCU">ISCU (Iron-Sulfur cluster scaffold homolog (E. coli))</OPTION><OPTION value="ITGA7">ITGA7 (Integrin, alpha 7)</OPTION><OPTION value="KBTBD13">KBTBD13 (Kelch repeat and BTB (POZ) domain containing 13)</OPTION><OPTION value="KIF1B">KIF1B (kinesin family member 1B)</OPTION><OPTION value="KLHL40">KLHL40 (Kelch-like family member 40)</OPTION><OPTION value="LAMA2">LAMA2 (Laminin-alpha 2 (merosin))</OPTION><OPTION value="LAMP2">LAMP2 (Lysosomal-associated membrane protein 2)</OPTION><OPTION value="LARGE">LARGE (LARGE like-glycosyltransferase)</OPTION><OPTION value="LDB3">LDB3 (LIM domain binding 3 (ZASP))</OPTION><OPTION value="LITAF">LITAF (lipopolysaccharide-induced TNF factor)</OPTION><OPTION value="LMNA">LMNA (Lamin A/C)</OPTION><OPTION value="MATR3">MATR3 (Matrin 3)</OPTION><OPTION value="MFN2">MFN2 (Mitofusin 2)</OPTION><OPTION value="MICU1">MICU1 (Mitochondrial calcium uptake 1)</OPTION><OPTION value="MPZ">MPZ (Myelin protein zero)</OPTION><OPTION value="MSTN">MSTN (Myostatin)</OPTION><OPTION value="MTM1">MTM1 (Myotubularin 1)</OPTION><OPTION value="MTMR14">MTMR14 (Myotubularin related protein 14)</OPTION><OPTION value="MTMR2">MTMR2 (myotubularin related protein 2)</OPTION><OPTION value="MUSK">MUSK (muscle, skeletal, receptor tyrosine kinase)</OPTION><OPTION value="MYBPC3">MYBPC3 (Myosin binding protein C, cardiac)</OPTION><OPTION value="MYH7">MYH7 (myosin, heavy chain 7, cardiac muscle, beta)</OPTION><OPTION value="MYL2">MYL2 (Myosin, light chain 2, regulatory, cardiac, slow)</OPTION><OPTION value="MYL3">MYL3 (Myosin, light chain 3, alkali; ventricular, skeletal, slow)</OPTION><OPTION value="MYOT">MYOT (Myotilin (Titin immunoglobulin domain))</OPTION><OPTION value="MYOZ1">MYOZ1 (Myozenin 1)</OPTION><OPTION value="MYOZ2">MYOZ2 (Myozenin 2)</OPTION><OPTION value="MYOZ3">MYOZ3 (Myozenin 3)</OPTION><OPTION value="MYPN">MYPN (Myopalladin)</OPTION><OPTION value="NDRG1">NDRG1 (N-myc downstream regulated 1)</OPTION><OPTION value="NEB">NEB (Nebulin)</OPTION><OPTION value="NEFL">NEFL (Neurofilament, light polypeptide)</OPTION><OPTION value="NGF">NGF (nerve growth factor (beta polypeptide))</OPTION><OPTION value="NTRK1">NTRK1 (neurotrophic tyrosine kinase, receptor, type 1)</OPTION><OPTION value="PABPN1">PABPN1 (PolyA binding protein, nuclear 1)</OPTION><OPTION value="PDK3">PDK3 (Pyruvate dehydrogenase kinase, isozyme 3)</OPTION><OPTION value="PDLIM3">PDLIM3 (PDZ and LIM domain 3)</OPTION><OPTION value="PLEC">PLEC (Plectin)</OPTION><OPTION value="PLEKHG5">PLEKHG5 (pleckstrin homology domain containing, family G (with RhoGef do...))</OPTION><OPTION value="PMP22">PMP22 (Peripheral myelin protein 22)</OPTION><OPTION value="POMGNT1">POMGNT1 (Protein O-linked Mannose beta1,2-N-acetylGlucosaminylTransferase)</OPTION><OPTION value="POMT1">POMT1 (Protein O-Mannosyltransferase 1)</OPTION><OPTION value="POMT2">POMT2 (Protein O-Mannosyltransferase 2)</OPTION><OPTION value="PRPS1">PRPS1 (phosphoribosyl pyrophosphate synthetase 1)</OPTION><OPTION value="PRX">PRX (periaxin)</OPTION><OPTION value="PTRF">PTRF (Polymerase I and Transcript Release Factor (cavin-1))</OPTION><OPTION value="RAB7A">RAB7A (RAB7A, member RAS oncogene family)</OPTION><OPTION value="RAPSN">RAPSN (Receptor-associated protein of the synapse)</OPTION><OPTION value="RYR1">RYR1 (RYanodine Receptor 1 (skeletal))</OPTION><OPTION value="SBF2">SBF2 (SET binding factor 2)</OPTION><OPTION value="SEPN1">SEPN1 (Selenoprotein 1)</OPTION><OPTION value="SEPT9">SEPT9 (septin 9)</OPTION><OPTION value="SETX">SETX (senataxin)</OPTION><OPTION value="SGCA">SGCA (Sarcoglycan-alpha)</OPTION><OPTION value="SGCB">SGCB (Sarcoglycan-beta)</OPTION><OPTION value="SGCD">SGCD (Sarcoglycan-delta)</OPTION><OPTION value="SGCE">SGCE (Sarcoglycan-epsilon)</OPTION><OPTION value="SGCG">SGCG (Sarcoglycan-gamma)</OPTION><OPTION value="SGCZ">SGCZ (Sarcoglycan-zeta)</OPTION><OPTION value="SH3TC2">SH3TC2 (SH3 domain and tetratricopeptide repeats 2)</OPTION><OPTION value="SLC12A6">SLC12A6 (solute carrier family 12 (potassium/chloride transporters), mem...))</OPTION><OPTION value="SMCHD1">SMCHD1 (Structural maintenance of chromosomes flexible hinge domain cont...)</OPTION><OPTION value="SMN1">SMN1 (Survival Motor Neuron 1)</OPTION><OPTION value="SOX10">SOX10 (SRY (sex determining region Y)-box 10)</OPTION><OPTION value="SPTLC1">SPTLC1 (serine palmitoyltransferase, long chain base subunit 1)</OPTION><OPTION value="SPTLC2">SPTLC2 (serine palmitoyltransferase, long chain base subunit 2)</OPTION><OPTION value="SSPN">SSPN (Sarcospan)</OPTION><OPTION value="SYNE1">SYNE1 (Spectrin repeat containing, Nuclear Envelope 1)</OPTION><OPTION value="SYNE2">SYNE2 (Spectrin repeat containing, Nuclear Envelope 2)</OPTION><OPTION value="TCAP">TCAP (Titin-cap (telethonin))</OPTION><OPTION value="TNNI2">TNNI2 (Troponin I type 2)</OPTION><OPTION value="TNNI3">TNNI3 (Troponin I type 3 (cardiac))</OPTION><OPTION value="TNNT1">TNNT1 (Troponin T type 1)</OPTION><OPTION value="TNNT2">TNNT2 (Troponin T type 2 (cardiac))</OPTION><OPTION value="TNNT3">TNNT3 (Troponin T type 3)</OPTION><OPTION value="TNPO3">TNPO3 (Transportin 3)</OPTION><OPTION value="TPM1">TPM1 (tropomyosin 1 (alpha))</OPTION><OPTION value="TPM2">TPM2 (Tropomyosin 2)</OPTION><OPTION value="TPM3">TPM3 (Tropomyosin 3)</OPTION><OPTION value="TRAPPC11">TRAPPC11 (Trafficking protein particle complex 11)</OPTION><OPTION value="TRDN">TRDN (Triadin)</OPTION><OPTION value="TRIM32">TRIM32 (Tripartite motif-containing 32)</OPTION><OPTION value="TTN">TTN (Titin)</OPTION><OPTION value="TTR">TTR (Transthyretin)</OPTION><OPTION value="VCP">VCP (Valosin-containing protein)</OPTION><OPTION value="VMA21">VMA21 (VMA21 vacuolar H+-ATPase homolog (S. cerevisiae))</OPTION><OPTION value="WNK1">WNK1 (WNK lysine deficient protein kinase 1)</OPTION><OPTION value="YARS">YARS (tyrosyl-tRNA synthetase)</OPTION><OPTION value="ZMPSTE24">ZMPSTE24 (Zinc MetalloPeptidase (STE24 homolog, yeast))</OPTION></SELECT><INPUT type="submit" value="Switch"></FORM>';
      document.getElementById('gene_name').innerHTML=varForm;
    }

    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="./inc-js-openwindow.php"></SCRIPT>
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD width="150">
      <IMG src="./gfx/LOVD_logo130x50.jpg" alt="LOVD - Leiden Open Variation Database" width="130" height="50">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">Leiden Muscular Dystrophy pages</H2>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.2.0 Build 35 [ <A href="./status.php">Current LOVD status</A> ]<BR>
      <A href="./submitters.php?action=register"><B>Register as submitter</B></A> | <A href="./account_login.php"><B>Log in</B></A><BR>
    </TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('./gfx/tab_fill.png');">
      <IMG src="./gfx/tab_0F.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/home.php"><IMG src="./gfx/tab_home_F.png" alt="Home" title="Home" width="41" height="30" align="left" id="navHome" border="0"></A>
      <IMG src="./gfx/tab_FB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/variants.php?action=search_unique"><IMG src="./gfx/tab_variants_B.png" alt="View unique variants" title="View unique variants" width="56" height="30" align="left" id="navVariants" border="0" onmouseover="lovd_imageSwitch('navVariants', 'H');" onmouseout="lovd_imageSwitch('navVariants', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submitters.php?action=public_list"><IMG src="./gfx/tab_submitters_B.png" alt="Public list of submitters" title="Public list of submitters" width="75" height="30" align="left" id="navSubmitters" border="0" onmouseover="lovd_imageSwitch('navSubmitters', 'H');" onmouseout="lovd_imageSwitch('navSubmitters', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submit.php"><IMG src="./gfx/tab_submit_B.png" alt="Submit new data" title="Submit new data" width="50" height="30" align="left" id="navSubmit" border="0" onmouseover="lovd_imageSwitch('navSubmit', 'H');" onmouseout="lovd_imageSwitch('navSubmit', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/docs/index.php"><IMG src="./gfx/tab_docs_B.png" alt="LOVD manual table of contents" title="LOVD manual table of contents" width="110" height="30" align="left" id="navDocs" border="0" onmouseover="lovd_imageSwitch('navDocs', 'H');" onmouseout="lovd_imageSwitch('navDocs', 'B');"></A>
      <IMG src="./gfx/tab_B0.png" alt="" width="33" height="30" align="left">
    </TD>
  </TR>
</TABLE>

<DIV style="padding : 5px; margin-bottom : 5px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="submenu">
  <TR>
    <TD>
      <TABLE border="0" cellpadding="0" cellspacing="0">
        <TR>
          <TD align="center"><A href="/nmdb2/home.php">Home</A></TD>
          <TD style="padding : 0px;">&nbsp;</TD>
          <TD align="center" style="background : #C8DCFA;"><A href="/nmdb2/home.php?action=switch_db">Switch&nbsp;gene</A></TD>
        </TR>
      </TABLE>
    </TD>
  </TR>
</TABLE>
</DIV>




<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD>








      <IMG src="./gfx/header_home_select.png" alt="Home - Select gene database" width="500" height="30"><BR>
      <BR>
      Please select a gene database:<BR>
      <FORM action="/nmdb2/home.php" id="SelectGeneDB" method="get">
        <SELECT name="select_db" onchange="document.getElementById('SelectGeneDB').submit();">
          <OPTION value="ACTA1">ACTA1 (ACTin, Alpha 1 (skeletal muscle))</OPTION>
          <OPTION value="ACTC1">ACTC1 (Actin, alpha, cardiac muscle 1)</OPTION>
          <OPTION value="AGRN">AGRN (Agrin)</OPTION>
          <OPTION value="ANKRD1">ANKRD1 (Ankyrin repeat domain 1 (cardiac muscle))</OPTION>
          <OPTION value="ANO5">ANO5 (Anoctamin 5)</OPTION>
          <OPTION value="ARHGEF10">ARHGEF10 (Rho guanine nucleotide exchange factor (GEF) 10)</OPTION>
          <OPTION value="ASAH1">ASAH1 (N-acylsphingosine amidohydrolase (acid ceramidase) 1)</OPTION>
          <OPTION value="ATL1">ATL1 (Atlastin GTPase 1)</OPTION>
          <OPTION value="B3GALNT2">B3GALNT2 (Beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION>
          <OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION>
          <OPTION value="BAG3">BAG3 (BCL2-associated athanogene 3)</OPTION>
          <OPTION value="BANF1">BANF1 (Barrier to autointegration factor 1)</OPTION>
          <OPTION value="BIN1">BIN1 (Bridging INtegrator 1)</OPTION>
          <OPTION value="BSCL2">BSCL2 (Berardinelli-Seip congenital lipodystrophy 2 (seipin))</OPTION>
          <OPTION value="CAPN3">CAPN3 (Calpain-3)</OPTION>
          <OPTION value="CAV3">CAV3 (Caveolin-3)</OPTION>
          <OPTION value="CCDC78">CCDC78 (Coiled-coil domain containing 78)</OPTION>
          <OPTION value="CCT5">CCT5 (Chaperonin containing TCP1, subunit 5 (epsilon))</OPTION>
          <OPTION value="CFL2">CFL2 (Cofilin 2)</OPTION>
          <OPTION value="CHAT">CHAT (Choline O-acetyltransferase)</OPTION>
          <OPTION value="CHKB">CHKB (Choline kinase beta)</OPTION>
          <OPTION value="CHRNA1">CHRNA1 (cholinergic receptor, nicotinic, alpha 1 (muscle))</OPTION>
          <OPTION value="CHRNB1">CHRNB1 (Cholinergic receptor, nicotinic, beta 1 (muscle))</OPTION>
          <OPTION value="CHRND">CHRND (Cholinergic receptor, nicotinic, delta)</OPTION>
          <OPTION value="CHRNE">CHRNE (Cholinergic receptor, nicotinic, epsilon)</OPTION>
          <OPTION value="CNTN1">CNTN1 (Contactin 1)</OPTION>
          <OPTION value="COL6A1">COL6A1 (Collagen type VI alpha 1)</OPTION>
          <OPTION value="COL6A2">COL6A2 (Collagen type VI alpha 2)</OPTION>
          <OPTION value="COL6A3">COL6A3 (Collagen type VI alpha 3)</OPTION>
          <OPTION value="COLQ">COLQ (Collagen-like tail subunit (single strand of homotrimer) of asymmetric acetylcholinesterase)</OPTION>
          <OPTION value="CRYAB">CRYAB (Crystallin, alpha-B)</OPTION>
          <OPTION value="CTDP1">CTDP1 (CTD (carboxy-terminal domain, RNA polymerase II, polypeptide A) phosphatase, subunit 1)</OPTION>
          <OPTION value="DAG1">DAG1 (Dystrophin-Associated Glycoprotein 1)</OPTION>
          <OPTION value="DCTN1">DCTN1 (dynactin 1)</OPTION>
          <OPTION value="DES">DES (Desmin)</OPTION>
          <OPTION value="DMD">DMD (Duchenne Muscular Dystrophy)</OPTION>
          <OPTION value="DMD_d">DMD_d (Duchenne Muscular Dystrophy (whole exon changes))</OPTION>
          <OPTION value="DNAJB6">DNAJB6 (DnaJ (Hsp40) homolog, subfamily B, member 6)</OPTION>
          <OPTION value="DNM2">DNM2 (Dynamin 2)</OPTION>
          <OPTION value="DOK7">DOK7 (Docking protein 7)</OPTION>
          <OPTION value="DPM3">DPM3 (Dolichyl-Phosphate Mannosyltransferase polypeptide 3)</OPTION>
          <OPTION value="DTNA">DTNA (Dystrobrevin alpha)</OPTION>
          <OPTION value="DUX4">DUX4 (Double homeobox 4)</OPTION>
          <OPTION value="DYSF">DYSF (Dysferlin)</OPTION>
          <OPTION value="EGR2">EGR2 (early growth response 2)</OPTION>
          <OPTION value="EMD">EMD (Emery-Dreifuss muscular dystrophy (emerin))</OPTION>
          <OPTION value="FAM134B">FAM134B (family with sequence similarity 134, member B)</OPTION>
          <OPTION value="FGD4">FGD4 (FYVE, RhoGEF and PH domain containing 4)</OPTION>
          <OPTION value="FHL1">FHL1 (Four and a Half LIM domains 1)</OPTION>
          <OPTION value="FIG4">FIG4 (FIG4 homolog, SAC1 lipid phosphatase domain containing (S. cerevisiae))</OPTION>
          <OPTION value="FKRP">FKRP (Fukutin-Related Protein)</OPTION>
          <OPTION value="FKTN">FKTN (Fukutin)</OPTION>
          <OPTION value="FLNC">FLNC (Filamin C)</OPTION>
          <OPTION value="GAN">GAN (Gigaxonin)</OPTION>
          <OPTION value="GARS">GARS (glycyl-tRNA synthetase)</OPTION>
          <OPTION value="GDAP1">GDAP1 (ganglioside induced differentiation associated protein 1)</OPTION>
          <OPTION value="GFPT1">GFPT1 (Glutamine-fructose-6-phosphate transaminase 1)</OPTION>
          <OPTION value="GJB1">GJB1 (gap junction protein, beta 1, 32kDa)</OPTION>
          <OPTION value="GK">GK (Glycerol Kinase)</OPTION>
          <OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION>
          <OPTION value="GNB4">GNB4 (Guanine nucleotide binding protein (G protein), beta polypeptide 4)</OPTION>
          <OPTION value="GNE">GNE (glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase)</OPTION>
          <OPTION value="GTDC2">GTDC2 (Glycosyltransferase-like domain containing 2)</OPTION>
          <OPTION value="HSPB1">HSPB1 (heat shock 27kDa protein 1)</OPTION>
          <OPTION value="HSPB3">HSPB3 (heat shock 27kDa protein 3)</OPTION>
          <OPTION value="HSPB8">HSPB8 (heat shock 22kDa protein 8)</OPTION>
          <OPTION value="IGHMBP2">IGHMBP2 (Immunoglobulin mu binding protein 2)</OPTION>
          <OPTION value="IKBKAP">IKBKAP (inhibitor of kappa light polypeptide gene enhancer in B-cells, kinase complex-associated ...)</OPTION>
          <OPTION value="ISCU">ISCU (Iron-Sulfur cluster scaffold homolog (E. coli))</OPTION>
          <OPTION value="ITGA7">ITGA7 (Integrin, alpha 7)</OPTION>
          <OPTION value="KBTBD13">KBTBD13 (Kelch repeat and BTB (POZ) domain containing 13)</OPTION>
          <OPTION value="KIF1B">KIF1B (kinesin family member 1B)</OPTION>
          <OPTION value="KLHL40">KLHL40 (Kelch-like family member 40)</OPTION>
          <OPTION value="LAMA2">LAMA2 (Laminin-alpha 2 (merosin))</OPTION>
          <OPTION value="LAMP2">LAMP2 (Lysosomal-associated membrane protein 2)</OPTION>
          <OPTION value="LARGE">LARGE (LARGE like-glycosyltransferase)</OPTION>
          <OPTION value="LDB3">LDB3 (LIM domain binding 3 (ZASP))</OPTION>
          <OPTION value="LITAF">LITAF (lipopolysaccharide-induced TNF factor)</OPTION>
          <OPTION value="LMNA">LMNA (Lamin A/C)</OPTION>
          <OPTION value="MATR3">MATR3 (Matrin 3)</OPTION>
          <OPTION value="MFN2">MFN2 (Mitofusin 2)</OPTION>
          <OPTION value="MICU1">MICU1 (Mitochondrial calcium uptake 1)</OPTION>
          <OPTION value="MPZ">MPZ (Myelin protein zero)</OPTION>
          <OPTION value="MSTN">MSTN (Myostatin)</OPTION>
          <OPTION value="MTM1">MTM1 (Myotubularin 1)</OPTION>
          <OPTION value="MTMR14">MTMR14 (Myotubularin related protein 14)</OPTION>
          <OPTION value="MTMR2">MTMR2 (myotubularin related protein 2)</OPTION>
          <OPTION value="MUSK">MUSK (muscle, skeletal, receptor tyrosine kinase)</OPTION>
          <OPTION value="MYBPC3">MYBPC3 (Myosin binding protein C, cardiac)</OPTION>
          <OPTION value="MYH7">MYH7 (myosin, heavy chain 7, cardiac muscle, beta)</OPTION>
          <OPTION value="MYL2">MYL2 (Myosin, light chain 2, regulatory, cardiac, slow)</OPTION>
          <OPTION value="MYL3">MYL3 (Myosin, light chain 3, alkali; ventricular, skeletal, slow)</OPTION>
          <OPTION value="MYOT">MYOT (Myotilin (Titin immunoglobulin domain))</OPTION>
          <OPTION value="MYOZ1">MYOZ1 (Myozenin 1)</OPTION>
          <OPTION value="MYOZ2">MYOZ2 (Myozenin 2)</OPTION>
          <OPTION value="MYOZ3">MYOZ3 (Myozenin 3)</OPTION>
          <OPTION value="MYPN">MYPN (Myopalladin)</OPTION>
          <OPTION value="NDRG1">NDRG1 (N-myc downstream regulated 1)</OPTION>
          <OPTION value="NEB">NEB (Nebulin)</OPTION>
          <OPTION value="NEFL">NEFL (Neurofilament, light polypeptide)</OPTION>
          <OPTION value="NGF">NGF (nerve growth factor (beta polypeptide))</OPTION>
          <OPTION value="NTRK1">NTRK1 (neurotrophic tyrosine kinase, receptor, type 1)</OPTION>
          <OPTION value="PABPN1">PABPN1 (PolyA binding protein, nuclear 1)</OPTION>
          <OPTION value="PDK3">PDK3 (Pyruvate dehydrogenase kinase, isozyme 3)</OPTION>
          <OPTION value="PDLIM3">PDLIM3 (PDZ and LIM domain 3)</OPTION>
          <OPTION value="PLEC">PLEC (Plectin)</OPTION>
          <OPTION value="PLEKHG5">PLEKHG5 (pleckstrin homology domain containing, family G (with RhoGef domain) member 5)</OPTION>
          <OPTION value="PMP22">PMP22 (Peripheral myelin protein 22)</OPTION>
          <OPTION value="POMGNT1">POMGNT1 (Protein O-linked Mannose beta1,2-N-acetylGlucosaminylTransferase)</OPTION>
          <OPTION value="POMT1">POMT1 (Protein O-Mannosyltransferase 1)</OPTION>
          <OPTION value="POMT2">POMT2 (Protein O-Mannosyltransferase 2)</OPTION>
          <OPTION value="PRPS1">PRPS1 (phosphoribosyl pyrophosphate synthetase 1)</OPTION>
          <OPTION value="PRX">PRX (periaxin)</OPTION>
          <OPTION value="PTRF">PTRF (Polymerase I and Transcript Release Factor (cavin-1))</OPTION>
          <OPTION value="RAB7A">RAB7A (RAB7A, member RAS oncogene family)</OPTION>
          <OPTION value="RAPSN">RAPSN (Receptor-associated protein of the synapse)</OPTION>
          <OPTION value="RYR1">RYR1 (RYanodine Receptor 1 (skeletal))</OPTION>
          <OPTION value="SBF2">SBF2 (SET binding factor 2)</OPTION>
          <OPTION value="SEPN1">SEPN1 (Selenoprotein 1)</OPTION>
          <OPTION value="SEPT9">SEPT9 (septin 9)</OPTION>
          <OPTION value="SETX">SETX (senataxin)</OPTION>
          <OPTION value="SGCA">SGCA (Sarcoglycan-alpha)</OPTION>
          <OPTION value="SGCB">SGCB (Sarcoglycan-beta)</OPTION>
          <OPTION value="SGCD">SGCD (Sarcoglycan-delta)</OPTION>
          <OPTION value="SGCE">SGCE (Sarcoglycan-epsilon)</OPTION>
          <OPTION value="SGCG">SGCG (Sarcoglycan-gamma)</OPTION>
          <OPTION value="SGCZ">SGCZ (Sarcoglycan-zeta)</OPTION>
          <OPTION value="SH3TC2">SH3TC2 (SH3 domain and tetratricopeptide repeats 2)</OPTION>
          <OPTION value="SLC12A6">SLC12A6 (solute carrier family 12 (potassium/chloride transporters), member 6)</OPTION>
          <OPTION value="SMCHD1">SMCHD1 (Structural maintenance of chromosomes flexible hinge domain containing 1)</OPTION>
          <OPTION value="SMN1">SMN1 (Survival Motor Neuron 1)</OPTION>
          <OPTION value="SOX10">SOX10 (SRY (sex determining region Y)-box 10)</OPTION>
          <OPTION value="SPTLC1">SPTLC1 (serine palmitoyltransferase, long chain base subunit 1)</OPTION>
          <OPTION value="SPTLC2">SPTLC2 (serine palmitoyltransferase, long chain base subunit 2)</OPTION>
          <OPTION value="SSPN">SSPN (Sarcospan)</OPTION>
          <OPTION value="SYNE1">SYNE1 (Spectrin repeat containing, Nuclear Envelope 1)</OPTION>
          <OPTION value="SYNE2">SYNE2 (Spectrin repeat containing, Nuclear Envelope 2)</OPTION>
          <OPTION value="TCAP">TCAP (Titin-cap (telethonin))</OPTION>
          <OPTION value="TNNI2">TNNI2 (Troponin I type 2)</OPTION>
          <OPTION value="TNNI3">TNNI3 (Troponin I type 3 (cardiac))</OPTION>
          <OPTION value="TNNT1">TNNT1 (Troponin T type 1)</OPTION>
          <OPTION value="TNNT2">TNNT2 (Troponin T type 2 (cardiac))</OPTION>
          <OPTION value="TNNT3">TNNT3 (Troponin T type 3)</OPTION>
          <OPTION value="TNPO3">TNPO3 (Transportin 3)</OPTION>
          <OPTION value="TPM1">TPM1 (tropomyosin 1 (alpha))</OPTION>
          <OPTION value="TPM2">TPM2 (Tropomyosin 2)</OPTION>
          <OPTION value="TPM3">TPM3 (Tropomyosin 3)</OPTION>
          <OPTION value="TRAPPC11">TRAPPC11 (Trafficking protein particle complex 11)</OPTION>
          <OPTION value="TRDN">TRDN (Triadin)</OPTION>
          <OPTION value="TRIM32">TRIM32 (Tripartite motif-containing 32)</OPTION>
          <OPTION value="TTN">TTN (Titin)</OPTION>
          <OPTION value="TTR">TTR (Transthyretin)</OPTION>
          <OPTION value="VCP">VCP (Valosin-containing protein)</OPTION>
          <OPTION value="VMA21">VMA21 (VMA21 vacuolar H+-ATPase homolog (S. cerevisiae))</OPTION>
          <OPTION value="WNK1">WNK1 (WNK lysine deficient protein kinase 1)</OPTION>
          <OPTION value="YARS">YARS (tyrosyl-tRNA synthetase)</OPTION>
          <OPTION value="ZMPSTE24">ZMPSTE24 (Zinc MetalloPeptidase (STE24 homolog, yeast))</OPTION>
        </SELECT><BR>
        <INPUT type="submit" value="Select gene database">
      </FORM>









    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/2.0/" target="_blank">LOVD v.2.0</A> Build 35<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_update_newest_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>

<SCRIPT type="text/javascript">
  <!--
  objImg = document.getElementById('mapping_progress');

function lovd_HTTPRequest (sURL) {
    // Create HTTP request object.
    var objHTTP;
    try {
        // W3C standard.
        objHTTP = new XMLHttpRequest();
    } catch (e) {
        // Internet Explorer?
        try {
            objHTTP = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                objHTTP = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
                // Ok, last try!
                try {
                    objHTTP = window.createRequest();
                } catch (e) {
                    // Never mind.
                    objHTTP = false;
                }
            }
        }
    }

    if (objHTTP) {
        objHTTP.open("GET", sURL, false);
        objHTTP.send(null);
        return objHTTP;

    } else {
        return false;
    }
}



  function lovd_mapVariants () {
    // Request file that will do the actual work.
    objHTTP = lovd_HTTPRequest("http://www.dmd.nl/nmdb2/ajax-map_variants.php");

    if (!objHTTP || objHTTP.status != 200) {
        // Don't try again.
        objImg.src = "./gfx/lovd_mapping_99.png";
        objImg.title = "There was a problem with LOVD while mapping variants to the genome.";
    } else {
        aResponse = objHTTP.responseText.split("\t");
        // 2010-05-03; 2.0-26; Verify output, to prevent PHP errors from freaking out the browser (= every 50 microseconds a new request).
        // Took (and shortened) the "is_numeric()" implementation from http://phpjs.org/functions/is_numeric:449 (thanks guys).
        if (aResponse.length == 2 && !isNaN(aResponse[0])) {
            objImg.src = "./gfx/lovd_mapping_" + aResponse[0] + ".png";
            objImg.title = aResponse[1];

            if (aResponse[1] != "All done!") {
                setTimeout("lovd_mapVariants()", 50);
            } else {
                objImg.setAttribute("onclick", "lovd_mapVariants();");
            }
        } else {
            objImg.title = "Error occured: " + objHTTP.responseText;
        }
    }
  }

objImg.setAttribute("onclick", "lovd_mapVariants();");
  // -->
</SCRIPT>

</BODY>
</HTML>
"""

ACTA1_GENE_HOMEPAGE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>ACTA1 homepage - Leiden Muscular Dystrophy pages - Leiden Open Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
  <META name="Author" content="LOVD development team, LUMC, Netherlands">
  <META name="Generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <LINK rel="stylesheet" type="text/css" href="./styles.css">
  <LINK rel="shortcut icon" href="./favicon.ico">
  <LINK rel="alternate" type="application/atom+xml" title="Leiden Muscular Dystrophy pages Atom 1.0 feed" href="./api/feed.php" />

  <SCRIPT type="text/javascript">
    <!--
    navHome_B     = new Image();
    navHome_B.src = './gfx/tab_home_B.png';
    navHome_H     = new Image();
    navHome_H.src = './gfx/tab_home_H.png';
    navVariants_B     = new Image();
    navVariants_B.src = './gfx/tab_variants_B.png';
    navVariants_H     = new Image();
    navVariants_H.src = './gfx/tab_variants_H.png';
    navSubmitters_B     = new Image();
    navSubmitters_B.src = './gfx/tab_submitters_B.png';
    navSubmitters_H     = new Image();
    navSubmitters_H.src = './gfx/tab_submitters_H.png';
    navSubmit_B     = new Image();
    navSubmit_B.src = './gfx/tab_submit_B.png';
    navSubmit_H     = new Image();
    navSubmit_H.src = './gfx/tab_submit_H.png';
    navDocs_B     = new Image();
    navDocs_B.src = './gfx/tab_docs_B.png';
    navDocs_H     = new Image();
    navDocs_H.src = './gfx/tab_docs_H.png';

    // Used for tab images.
    function lovd_imageSwitch (image_id, image_mode) {
      document.getElementById(image_id).src = eval(image_id + '_' + image_mode + '.src');
    }

    function lovd_switchGeneInline () {
      varForm = '<FORM action="/nmdb2/home.php" id="SelectGeneDBInline" method="get" style="margin : 0px;"><SELECT name="select_db" onchange="document.getElementById(\'SelectGeneDBInline\').submit();"><OPTION value="ACTA1" selected>ACTA1 (ACTin, Alpha 1 (skeletal muscle))</OPTION><OPTION value="ACTC1">ACTC1 (Actin, alpha, cardiac muscle 1)</OPTION><OPTION value="AGRN">AGRN (Agrin)</OPTION><OPTION value="ANKRD1">ANKRD1 (Ankyrin repeat domain 1 (cardiac muscle))</OPTION><OPTION value="ANO5">ANO5 (Anoctamin 5)</OPTION><OPTION value="ARHGEF10">ARHGEF10 (Rho guanine nucleotide exchange factor (GEF) 10)</OPTION><OPTION value="ASAH1">ASAH1 (N-acylsphingosine amidohydrolase (acid ceramidase) 1)</OPTION><OPTION value="ATL1">ATL1 (Atlastin GTPase 1)</OPTION><OPTION value="B3GALNT2">B3GALNT2 (Beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION><OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION><OPTION value="BAG3">BAG3 (BCL2-associated athanogene 3)</OPTION><OPTION value="BANF1">BANF1 (Barrier to autointegration factor 1)</OPTION><OPTION value="BIN1">BIN1 (Bridging INtegrator 1)</OPTION><OPTION value="BSCL2">BSCL2 (Berardinelli-Seip congenital lipodystrophy 2 (seipin))</OPTION><OPTION value="CAPN3">CAPN3 (Calpain-3)</OPTION><OPTION value="CAV3">CAV3 (Caveolin-3)</OPTION><OPTION value="CCDC78">CCDC78 (Coiled-coil domain containing 78)</OPTION><OPTION value="CCT5">CCT5 (Chaperonin containing TCP1, subunit 5 (epsilon))</OPTION><OPTION value="CFL2">CFL2 (Cofilin 2)</OPTION><OPTION value="CHAT">CHAT (Choline O-acetyltransferase)</OPTION><OPTION value="CHKB">CHKB (Choline kinase beta)</OPTION><OPTION value="CHRNA1">CHRNA1 (cholinergic receptor, nicotinic, alpha 1 (muscle))</OPTION><OPTION value="CHRNB1">CHRNB1 (Cholinergic receptor, nicotinic, beta 1 (muscle))</OPTION><OPTION value="CHRND">CHRND (Cholinergic receptor, nicotinic, delta)</OPTION><OPTION value="CHRNE">CHRNE (Cholinergic receptor, nicotinic, epsilon)</OPTION><OPTION value="CNTN1">CNTN1 (Contactin 1)</OPTION><OPTION value="COL6A1">COL6A1 (Collagen type VI alpha 1)</OPTION><OPTION value="COL6A2">COL6A2 (Collagen type VI alpha 2)</OPTION><OPTION value="COL6A3">COL6A3 (Collagen type VI alpha 3)</OPTION><OPTION value="COLQ">COLQ (Collagen-like tail subunit (single strand of homotrimer) of asymme...))</OPTION><OPTION value="CRYAB">CRYAB (Crystallin, alpha-B)</OPTION><OPTION value="CTDP1">CTDP1 (CTD (carboxy-terminal domain, RNA polymerase II, polypeptide A) p...))</OPTION><OPTION value="DAG1">DAG1 (Dystrophin-Associated Glycoprotein 1)</OPTION><OPTION value="DCTN1">DCTN1 (dynactin 1)</OPTION><OPTION value="DES">DES (Desmin)</OPTION><OPTION value="DMD">DMD (Duchenne Muscular Dystrophy)</OPTION><OPTION value="DMD_d">DMD_d (Duchenne Muscular Dystrophy (whole exon changes))</OPTION><OPTION value="DNAJB6">DNAJB6 (DnaJ (Hsp40) homolog, subfamily B, member 6)</OPTION><OPTION value="DNM2">DNM2 (Dynamin 2)</OPTION><OPTION value="DOK7">DOK7 (Docking protein 7)</OPTION><OPTION value="DPM3">DPM3 (Dolichyl-Phosphate Mannosyltransferase polypeptide 3)</OPTION><OPTION value="DTNA">DTNA (Dystrobrevin alpha)</OPTION><OPTION value="DUX4">DUX4 (Double homeobox 4)</OPTION><OPTION value="DYSF">DYSF (Dysferlin)</OPTION><OPTION value="EGR2">EGR2 (early growth response 2)</OPTION><OPTION value="EMD">EMD (Emery-Dreifuss muscular dystrophy (emerin))</OPTION><OPTION value="FAM134B">FAM134B (family with sequence similarity 134, member B)</OPTION><OPTION value="FGD4">FGD4 (FYVE, RhoGEF and PH domain containing 4)</OPTION><OPTION value="FHL1">FHL1 (Four and a Half LIM domains 1)</OPTION><OPTION value="FIG4">FIG4 (FIG4 homolog, SAC1 lipid phosphatase domain containing (S. cerevis...))</OPTION><OPTION value="FKRP">FKRP (Fukutin-Related Protein)</OPTION><OPTION value="FKTN">FKTN (Fukutin)</OPTION><OPTION value="FLNC">FLNC (Filamin C)</OPTION><OPTION value="GAN">GAN (Gigaxonin)</OPTION><OPTION value="GARS">GARS (glycyl-tRNA synthetase)</OPTION><OPTION value="GDAP1">GDAP1 (ganglioside induced differentiation associated protein 1)</OPTION><OPTION value="GFPT1">GFPT1 (Glutamine-fructose-6-phosphate transaminase 1)</OPTION><OPTION value="GJB1">GJB1 (gap junction protein, beta 1, 32kDa)</OPTION><OPTION value="GK">GK (Glycerol Kinase)</OPTION><OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION><OPTION value="GNB4">GNB4 (Guanine nucleotide binding protein (G protein), beta polypeptide 4)</OPTION><OPTION value="GNE">GNE (glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase)</OPTION><OPTION value="GTDC2">GTDC2 (Glycosyltransferase-like domain containing 2)</OPTION><OPTION value="HSPB1">HSPB1 (heat shock 27kDa protein 1)</OPTION><OPTION value="HSPB3">HSPB3 (heat shock 27kDa protein 3)</OPTION><OPTION value="HSPB8">HSPB8 (heat shock 22kDa protein 8)</OPTION><OPTION value="IGHMBP2">IGHMBP2 (Immunoglobulin mu binding protein 2)</OPTION><OPTION value="IKBKAP">IKBKAP (inhibitor of kappa light polypeptide gene enhancer in B-cells, k...)</OPTION><OPTION value="ISCU">ISCU (Iron-Sulfur cluster scaffold homolog (E. coli))</OPTION><OPTION value="ITGA7">ITGA7 (Integrin, alpha 7)</OPTION><OPTION value="KBTBD13">KBTBD13 (Kelch repeat and BTB (POZ) domain containing 13)</OPTION><OPTION value="KIF1B">KIF1B (kinesin family member 1B)</OPTION><OPTION value="KLHL40">KLHL40 (Kelch-like family member 40)</OPTION><OPTION value="LAMA2">LAMA2 (Laminin-alpha 2 (merosin))</OPTION><OPTION value="LAMP2">LAMP2 (Lysosomal-associated membrane protein 2)</OPTION><OPTION value="LARGE">LARGE (LARGE like-glycosyltransferase)</OPTION><OPTION value="LDB3">LDB3 (LIM domain binding 3 (ZASP))</OPTION><OPTION value="LITAF">LITAF (lipopolysaccharide-induced TNF factor)</OPTION><OPTION value="LMNA">LMNA (Lamin A/C)</OPTION><OPTION value="MATR3">MATR3 (Matrin 3)</OPTION><OPTION value="MFN2">MFN2 (Mitofusin 2)</OPTION><OPTION value="MICU1">MICU1 (Mitochondrial calcium uptake 1)</OPTION><OPTION value="MPZ">MPZ (Myelin protein zero)</OPTION><OPTION value="MSTN">MSTN (Myostatin)</OPTION><OPTION value="MTM1">MTM1 (Myotubularin 1)</OPTION><OPTION value="MTMR14">MTMR14 (Myotubularin related protein 14)</OPTION><OPTION value="MTMR2">MTMR2 (myotubularin related protein 2)</OPTION><OPTION value="MUSK">MUSK (muscle, skeletal, receptor tyrosine kinase)</OPTION><OPTION value="MYBPC3">MYBPC3 (Myosin binding protein C, cardiac)</OPTION><OPTION value="MYH7">MYH7 (myosin, heavy chain 7, cardiac muscle, beta)</OPTION><OPTION value="MYL2">MYL2 (Myosin, light chain 2, regulatory, cardiac, slow)</OPTION><OPTION value="MYL3">MYL3 (Myosin, light chain 3, alkali; ventricular, skeletal, slow)</OPTION><OPTION value="MYOT">MYOT (Myotilin (Titin immunoglobulin domain))</OPTION><OPTION value="MYOZ1">MYOZ1 (Myozenin 1)</OPTION><OPTION value="MYOZ2">MYOZ2 (Myozenin 2)</OPTION><OPTION value="MYOZ3">MYOZ3 (Myozenin 3)</OPTION><OPTION value="MYPN">MYPN (Myopalladin)</OPTION><OPTION value="NDRG1">NDRG1 (N-myc downstream regulated 1)</OPTION><OPTION value="NEB">NEB (Nebulin)</OPTION><OPTION value="NEFL">NEFL (Neurofilament, light polypeptide)</OPTION><OPTION value="NGF">NGF (nerve growth factor (beta polypeptide))</OPTION><OPTION value="NTRK1">NTRK1 (neurotrophic tyrosine kinase, receptor, type 1)</OPTION><OPTION value="PABPN1">PABPN1 (PolyA binding protein, nuclear 1)</OPTION><OPTION value="PDK3">PDK3 (Pyruvate dehydrogenase kinase, isozyme 3)</OPTION><OPTION value="PDLIM3">PDLIM3 (PDZ and LIM domain 3)</OPTION><OPTION value="PLEC">PLEC (Plectin)</OPTION><OPTION value="PLEKHG5">PLEKHG5 (pleckstrin homology domain containing, family G (with RhoGef do...))</OPTION><OPTION value="PMP22">PMP22 (Peripheral myelin protein 22)</OPTION><OPTION value="POMGNT1">POMGNT1 (Protein O-linked Mannose beta1,2-N-acetylGlucosaminylTransferase)</OPTION><OPTION value="POMT1">POMT1 (Protein O-Mannosyltransferase 1)</OPTION><OPTION value="POMT2">POMT2 (Protein O-Mannosyltransferase 2)</OPTION><OPTION value="PRPS1">PRPS1 (phosphoribosyl pyrophosphate synthetase 1)</OPTION><OPTION value="PRX">PRX (periaxin)</OPTION><OPTION value="PTRF">PTRF (Polymerase I and Transcript Release Factor (cavin-1))</OPTION><OPTION value="RAB7A">RAB7A (RAB7A, member RAS oncogene family)</OPTION><OPTION value="RAPSN">RAPSN (Receptor-associated protein of the synapse)</OPTION><OPTION value="RYR1">RYR1 (RYanodine Receptor 1 (skeletal))</OPTION><OPTION value="SBF2">SBF2 (SET binding factor 2)</OPTION><OPTION value="SEPN1">SEPN1 (Selenoprotein 1)</OPTION><OPTION value="SEPT9">SEPT9 (septin 9)</OPTION><OPTION value="SETX">SETX (senataxin)</OPTION><OPTION value="SGCA">SGCA (Sarcoglycan-alpha)</OPTION><OPTION value="SGCB">SGCB (Sarcoglycan-beta)</OPTION><OPTION value="SGCD">SGCD (Sarcoglycan-delta)</OPTION><OPTION value="SGCE">SGCE (Sarcoglycan-epsilon)</OPTION><OPTION value="SGCG">SGCG (Sarcoglycan-gamma)</OPTION><OPTION value="SGCZ">SGCZ (Sarcoglycan-zeta)</OPTION><OPTION value="SH3TC2">SH3TC2 (SH3 domain and tetratricopeptide repeats 2)</OPTION><OPTION value="SLC12A6">SLC12A6 (solute carrier family 12 (potassium/chloride transporters), mem...))</OPTION><OPTION value="SMCHD1">SMCHD1 (Structural maintenance of chromosomes flexible hinge domain cont...)</OPTION><OPTION value="SMN1">SMN1 (Survival Motor Neuron 1)</OPTION><OPTION value="SOX10">SOX10 (SRY (sex determining region Y)-box 10)</OPTION><OPTION value="SPTLC1">SPTLC1 (serine palmitoyltransferase, long chain base subunit 1)</OPTION><OPTION value="SPTLC2">SPTLC2 (serine palmitoyltransferase, long chain base subunit 2)</OPTION><OPTION value="SSPN">SSPN (Sarcospan)</OPTION><OPTION value="SYNE1">SYNE1 (Spectrin repeat containing, Nuclear Envelope 1)</OPTION><OPTION value="SYNE2">SYNE2 (Spectrin repeat containing, Nuclear Envelope 2)</OPTION><OPTION value="TCAP">TCAP (Titin-cap (telethonin))</OPTION><OPTION value="TNNI2">TNNI2 (Troponin I type 2)</OPTION><OPTION value="TNNI3">TNNI3 (Troponin I type 3 (cardiac))</OPTION><OPTION value="TNNT1">TNNT1 (Troponin T type 1)</OPTION><OPTION value="TNNT2">TNNT2 (Troponin T type 2 (cardiac))</OPTION><OPTION value="TNNT3">TNNT3 (Troponin T type 3)</OPTION><OPTION value="TNPO3">TNPO3 (Transportin 3)</OPTION><OPTION value="TPM1">TPM1 (tropomyosin 1 (alpha))</OPTION><OPTION value="TPM2">TPM2 (Tropomyosin 2)</OPTION><OPTION value="TPM3">TPM3 (Tropomyosin 3)</OPTION><OPTION value="TRAPPC11">TRAPPC11 (Trafficking protein particle complex 11)</OPTION><OPTION value="TRDN">TRDN (Triadin)</OPTION><OPTION value="TRIM32">TRIM32 (Tripartite motif-containing 32)</OPTION><OPTION value="TTN">TTN (Titin)</OPTION><OPTION value="TTR">TTR (Transthyretin)</OPTION><OPTION value="VCP">VCP (Valosin-containing protein)</OPTION><OPTION value="VMA21">VMA21 (VMA21 vacuolar H+-ATPase homolog (S. cerevisiae))</OPTION><OPTION value="WNK1">WNK1 (WNK lysine deficient protein kinase 1)</OPTION><OPTION value="YARS">YARS (tyrosyl-tRNA synthetase)</OPTION><OPTION value="ZMPSTE24">ZMPSTE24 (Zinc MetalloPeptidase (STE24 homolog, yeast))</OPTION></SELECT><INPUT type="submit" value="Switch"></FORM>';
      document.getElementById('gene_name').innerHTML=varForm;
    }

    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="./inc-js-openwindow.php"></SCRIPT>
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD width="150">
      <IMG src="./gfx/LOVD_logo130x50.jpg" alt="LOVD - Leiden Open Variation Database" width="130" height="50">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">Leiden Muscular Dystrophy pages</H2>
      <H5 id="gene_name">ACTin, Alpha 1 (skeletal muscle) (ACTA1)&nbsp;<A href="#" onclick="javascript:lovd_switchGeneInline(); return false;"><IMG src="./gfx/lovd_database_switch_inline.png" width="23" height="23" alt="Switch gene" title="Switch gene database" align="top" border="0"></A></H5>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.2.0 Build 35 [ <A href="./status.php">Current LOVD status</A> ]<BR>
      <A href="./submitters.php?action=register"><B>Register as submitter</B></A> | <A href="./account_login.php"><B>Log in</B></A><BR>
    </TD>
  </TR>
  <TR>
    <TD width="150">&nbsp;</TD>
    <TD valign="top" colspan="2" style="padding-bottom : 2px;"><B>Curators: <A href="mailto:knowak@waimr.uwa.edu.au">Kristen Nowak</A> and <A href="mailto:nlaing@waimr.uwa.edu.au">Nigel Laing</A></B></TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('./gfx/tab_fill.png');">
      <IMG src="./gfx/tab_0F.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/home.php?select_db=ACTA1"><IMG src="./gfx/tab_home_F.png" alt="ACTA1 homepage" title="ACTA1 homepage" width="41" height="30" align="left" id="navHome" border="0"></A>
      <IMG src="./gfx/tab_FB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/variants.php?action=search_unique&amp;select_db=ACTA1"><IMG src="./gfx/tab_variants_B.png" alt="View unique variants" title="View unique variants" width="56" height="30" align="left" id="navVariants" border="0" onmouseover="lovd_imageSwitch('navVariants', 'H');" onmouseout="lovd_imageSwitch('navVariants', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submitters.php?action=public_list"><IMG src="./gfx/tab_submitters_B.png" alt="Public list of submitters" title="Public list of submitters" width="75" height="30" align="left" id="navSubmitters" border="0" onmouseover="lovd_imageSwitch('navSubmitters', 'H');" onmouseout="lovd_imageSwitch('navSubmitters', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submit.php"><IMG src="./gfx/tab_submit_B.png" alt="Submit new data" title="Submit new data" width="50" height="30" align="left" id="navSubmit" border="0" onmouseover="lovd_imageSwitch('navSubmit', 'H');" onmouseout="lovd_imageSwitch('navSubmit', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/docs/index.php"><IMG src="./gfx/tab_docs_B.png" alt="LOVD manual table of contents" title="LOVD manual table of contents" width="110" height="30" align="left" id="navDocs" border="0" onmouseover="lovd_imageSwitch('navDocs', 'H');" onmouseout="lovd_imageSwitch('navDocs', 'B');"></A>
      <IMG src="./gfx/tab_B0.png" alt="" width="33" height="30" align="left">
    </TD>
  </TR>
</TABLE>

<DIV style="padding : 5px; margin-bottom : 5px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="submenu">
  <TR>
    <TD>
      <TABLE border="0" cellpadding="0" cellspacing="0">
        <TR>
          <TD align="center" style="background : #C8DCFA;"><A href="/nmdb2/home.php">ACTA1&nbsp;homepage</A></TD>
          <TD style="padding : 0px;">&nbsp;</TD>
          <TD align="center"><A href="/nmdb2/home.php?action=switch_db">Switch&nbsp;gene</A></TD>
        </TR>
      </TABLE>
    </TD>
  </TR>
</TABLE>
</DIV>




<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD>








      <DIV style="text-align : left;">This is the <b>Laing lab ACTA1 mutation database</b> originally initiated at the <a HREF='http://www.waimr.uwa.edu.au/'>Western Australian Institute for Medical Research (WAIMR)</a>. For purposes of user conveniance it has been combined with other muscle-related gene variant databases at the Leiden Muscular Dystrophy pages.<hr></DIV>

      <IMG src="./gfx/header_gene_homepage.png" alt="LOVD ACTA1 homepage" width="500" height="30"><BR>
      <BR>
      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">General information</TH></TR>
        <TR>
          <TH valign="top" width="275">Gene name</TH>
          <TD>ACTin, Alpha 1 (skeletal muscle)</TD></TR>
        <TR>
          <TH valign="top" width="275">Gene symbol</TH>
          <TD><B>ACTA1</B></TD></TR>
        <TR>
          <TH valign="top" width="275">Chromosome Location</TH>
          <TD>1q42.13</TD></TR>
        <TR>
          <TH valign="top" width="275">Database location</TH>
          <TD><a href='http://www.DMD.nl'>the Leiden Muscular Dystrophy pages</a></TD></TR>
        <TR>
          <TH valign="top" width="275">Curator</TH>
          <TD><A href="mailto:knowak@waimr.uwa.edu.au">Kristen Nowak</A> and <A href="mailto:nlaing@waimr.uwa.edu.au">Nigel Laing</A></TD></TR>
        <TR>
          <TH valign="top" width="275">PubMed references</TH>
          <TD>View all (unique) <A href="pubmed_references.php">PubMed references</A> in the ACTA1 database</TD></TR>
        <TR>
          <TH valign="top" width="275">Date of creation</TH>
          <TD>September 25, 2007</TD></TR>
        <TR>
          <TH valign="top" width="275">Last update</TH>
          <TD>April 29, 2014</TD></TR>
        <TR>
          <TH valign="top" width="275">Version</TH>
          <TD><B>ACTA1 140429</B></TD></TR>
        <TR>
          <TH valign="top" width="275">Add sequence variant</TH>
          <TD><A href="submit.php">Submit a sequence variant</A></TD></TR>
        <TR>
          <TH valign="top" width="275">First&nbsp;time&nbsp;submitters</TH>
          <TD><A href="submitters.php?action=register">Register here</A></TD></TR>
        <TR>
          <TH valign="top" width="275">Reference sequence file</TH>
          <TD><A href="http://www.dmd.nl/nmdb2/refseq/ACTA1_codingDNA.html">coding DNA reference sequence</A> for describing sequence variants</B></TD></TR>
        <TR>
          <TH valign="top" width="275">Genomic refseq ID</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?db=nucleotide&amp;sendto=t&amp;extrafeatpresent=1&amp;list_uids=NG_006672.1" target="_blank">NG_006672.1</A></TD></TR>
        <TR>
          <TH valign="top" width="275">Transcript refseq ID</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?db=nucleotide&amp;sendto=t&amp;extrafeatpresent=1&amp;list_uids=NM_001100.3" target="_blank">NM_001100.3</A></TD></TR>
        <TR>
          <TH valign="top" width="275">Exon/intron information</TH>
          <TD><A href="refseq/ACTA1_table.html" target="_blank">Exon/intron information table</A></TD></TR>
        <TR>
          <TH valign="top" width="275"><I>Total&nbsp;number&nbsp;of&nbsp;unique&nbsp;DNA&nbsp;variants&nbsp;reported</I></TH>
          <TD><B>231</B></TD></TR>
        <TR>
          <TH valign="top" width="275"><I>Total number of individuals with variant(s)</I></TH>
          <TD><B>362</B></TD></TR>
        <TR>
          <TH valign="top" width="275"><I>Total number of variants reported</I></TH>
          <TD><B>389</B></TD></TR>
        <TR>
          <TH valign="top" width="275">Subscribe to updates of this gene</TH>
          <TD><A href="api/feed.php?select_db=ACTA1" target="_blank"><IMG src="gfx/feed_icon.png" border="0"></A></TD></TR>
        <TR>
          <TH valign="top" width="275">NOTE</TH>
          <TD>This is the <b>Laing lab ACTA1 mutation database</b> originally initiated at the <a HREF='http://www.waimr.uwa.edu.au/'>Western Australian Institute for Medical Research (WAIMR)</a>. For purposes of user conveniance it has been combined with other muscle-related gene variant databases at the Leiden Muscular Dystrophy pages.<hr></TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">Graphical displays and utilities</TH></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_statistics.php">Summary tables</A></TH>
          <TD>Summary of all sequence variants in the ACTA1 database, sorted by type of variant (with graphical displays and statistics)</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="#" onclick="lovd_openWindow('./scripts/readingFrameChecker.php', 'ScriptsReadingFrameChecker', 800, 500); return false;" class="data">Reading-frame checker</A></TH>
          <TD>The Reading-frame checker generates a prediction of the effect of whole-exon changes</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="http://genome.ucsc.edu/cgi-bin/hgTracks?clade=mammal&amp;org=Human&amp;db=hg19&amp;position=chr1:229566942-229569893&amp;complement_hg19=1&amp;hgt.customText=http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FACTA1%3Fformat%3Dtext%2Fbed" target="_blank">UCSC Genome Browser</A></TH>
          <TD>Show variants in the UCSC Genome Browser (<A href="http://genome.ucsc.edu/cgi-bin/hgTracks?clade=mammal&amp;org=Human&amp;db=hg19&amp;position=chr1:229566942-229569893&amp;complement_hg19=1&amp;hgt.customText=http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FACTA1%3Fformat%3Dtext%2Fbed%26visibility%3D4" target="_blank">compact view</A>)</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="http://www.ensembl.org/Homo_sapiens/Location/View?r=1:229566942-229569893;contigviewbottom=url:http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FACTA1%3Fformat%3Dtext%2Fbed%26name%3D%2FACTA1%20variants=labels" target="_blank">Ensembl Genome Browser</A></TH>
          <TD>Show variants in the Ensembl Genome Browser (<A href="http://www.ensembl.org/Homo_sapiens/Location/View?r=1:229566942-229569893;contigviewbottom=url:http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FACTA1%3Fformat%3Dtext%2Fbed%26name%3D%2FACTA1%20variants=normal" target="_blank">compact view</A>)</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="http://www.ncbi.nlm.nih.gov/nuccore/NC_000001.10?report=graph&amp;v=229566942:229569893&amp;theme=Expanded&amp;content=7&amp;url=http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FACTA1%3Fformat%3Dtext%2Fbed" target="_blank">NCBI Sequence Viewer</A></TH>
          <TD>Show distribution histogram of variants in the NCBI Sequence Viewer</TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">Sequence variant tables</TH></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants.php?select_db=ACTA1&amp;action=view_unique">Unique sequence variants</A></TH>
          <TD>Listing of all unique sequence variants in the ACTA1 database, without patient data</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants.php?select_db=ACTA1&amp;action=view_all">Complete&nbsp;sequence&nbsp;variant&nbsp;listing</A></TH>
          <TD>Listing of all sequence variants in the ACTA1 database</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants.php?select_db=ACTA1&amp;action=search_unique&amp;search_pathogenic_=-">Variants&nbsp;with&nbsp;no&nbsp;known&nbsp;pathogenicity</A></TH>
          <TD>Listing of all ACTA1 variants reported to have no noticeable phenotypic effect (note: excluding variants of unknown effect)</TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">Search the database</TH></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_search.php?show=type">By&nbsp;type&nbsp;of&nbsp;variant</A></TH>
          <TD>View all sequence variants of a certain type</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_search.php?show=quick">Simple search</A></TH>
          <TD>Query the database by selecting the most important variables (exon number, type of variant, disease phenotype)</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_search.php?show=full">Advanced&nbsp;search</A></TH>
          <TD>Query the database by selecting a combination of variables</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_overview_origin.php">Based on patient origin</A></TH>
          <TD>View all variants based on your patient origin search terms</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_search.php?action=count_all">Search&nbsp;through&nbsp;hidden&nbsp;entries</A></TH>
          <TD>Find the number of variant entries in the database (including hidden entries) matching your search terms.</TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">Links to other resources</TH></TR>
        <TR>
          <TH valign="top" width="275">Homepage</TH>
          <TD><A href="http://www.DMD.nl/ACTA1" target="_blank">http://www.DMD.nl/ACTA1</A></TD></TR>
        <TR>
          <TH valign="top" width="275">HGNC</TH>
          <TD><A href="http://www.genenames.org/data/hgnc_data.php?hgnc_id=129" target="_blank">129</A></TD></TR>
        <TR>
          <TH valign="top" width="275">Entrez Gene</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=gene&amp;cmd=Retrieve&amp;dopt=full_report&amp;list_uids=58" target="_blank">58</A></TD></TR>
        <TR>
          <TH valign="top" width="275">OMIM - Gene</TH>
          <TD><A href="http://www.omim.org/entry/102610" target="_blank">102610</A></TD></TR>
        <TR>
          <TH valign="top" width="275">OMIM - Disease #1</TH>
          <TD><A href="http://www.omim.org/entry/161800" target="_blank">Nemaline Myopathy, type 3 (NEM-3)</A></TD></TR>
        <TR>
          <TH valign="top" width="275">OMIM - Disease #2</TH>
          <TD><A href="http://www.omim.org/entry/255310" target="_blank">Congenital Fiber-Type Disproportion (CFTD)</A></TD></TR>
        <TR>
          <TH valign="top" width="275">HGMD</TH>
          <TD><A href="http://www.hgmd.cf.ac.uk/ac/gene.php?gene=ACTA1" target="_blank">ACTA1</A></TD></TR>
        <TR>
          <TH valign="top" width="275">GeneCards</TH>
          <TD><A href="http://www.genecards.org/cgi-bin/carddisp.pl?gene=ACTA1" target="_blank">ACTA1</A></TD></TR>
        <TR>
          <TH valign="top" width="275">GeneTests</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/sites/GeneTests/lab/gene/ACTA1" target="_blank">ACTA1</A></TD></TR>
        <TR>
          <TH valign="top" width="275">External link</TH>
          <TD><A href="http://www.waimr.uwa.edu.au/" target="_blank">Western Australian Institute for Medical Research (WAIMR)</A></TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" class="S15">Copyright &amp; disclaimer</TH></TR>
        <TR class="S11">
          <TD>The contents of this LOVD database are the intellectual property of the respective curator(s). Any unauthorised use, copying, storage or distribution of this material without written permission from the curator(s) will lead to copyright infringement with possible ensuing litigation. Copyright &copy; 2014. All Rights Reserved. For further details, refer to Directive 96/9/EC of the European Parliament and the Council of March 11 (1996) on the legal protection of databases.<BR><BR>We have used all reasonable efforts to ensure that the information displayed on these pages and contained in the databases is of high quality. We make no warranty, express or implied, as to its accuracy or that the information is fit for a particular purpose, and will not be held responsible for any consequences arising out of any inaccuracies or omissions. Individuals, organisations and companies which use this database do so on the understanding that no liability whatsoever either direct or indirect shall rest upon the curator(s) or any of their employees or agents for the effects of any product, process or method that may be produced or adopted by any part, notwithstanding that the formulation of such product, process or method may be based upon information here provided.</TD></TR></TABLE>

<BR>







    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/2.0/" target="_blank">LOVD v.2.0</A> Build 35<BR>
  Enabled modules: recaptcha, showmaxdbid, mutalyzer<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_update_newest_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>

<SCRIPT type="text/javascript">
  <!--
  objImg = document.getElementById('mapping_progress');

function lovd_HTTPRequest (sURL) {
    // Create HTTP request object.
    var objHTTP;
    try {
        // W3C standard.
        objHTTP = new XMLHttpRequest();
    } catch (e) {
        // Internet Explorer?
        try {
            objHTTP = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                objHTTP = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
                // Ok, last try!
                try {
                    objHTTP = window.createRequest();
                } catch (e) {
                    // Never mind.
                    objHTTP = false;
                }
            }
        }
    }

    if (objHTTP) {
        objHTTP.open("GET", sURL, false);
        objHTTP.send(null);
        return objHTTP;

    } else {
        return false;
    }
}



  function lovd_mapVariants () {
    // Request file that will do the actual work.
    objHTTP = lovd_HTTPRequest("http://www.dmd.nl/nmdb2/ajax-map_variants.php");

    if (!objHTTP || objHTTP.status != 200) {
        // Don't try again.
        objImg.src = "./gfx/lovd_mapping_99.png";
        objImg.title = "There was a problem with LOVD while mapping variants to the genome.";
    } else {
        aResponse = objHTTP.responseText.split("\t");
        // 2010-05-03; 2.0-26; Verify output, to prevent PHP errors from freaking out the browser (= every 50 microseconds a new request).
        // Took (and shortened) the "is_numeric()" implementation from http://phpjs.org/functions/is_numeric:449 (thanks guys).
        if (aResponse.length == 2 && !isNaN(aResponse[0])) {
            objImg.src = "./gfx/lovd_mapping_" + aResponse[0] + ".png";
            objImg.title = aResponse[1];

            if (aResponse[1] != "All done!") {
                setTimeout("lovd_mapVariants()", 50);
            } else {
                objImg.setAttribute("onclick", "lovd_mapVariants();");
            }
        } else {
            objImg.title = "Error occured: " + objHTTP.responseText;
        }
    }
  }

objImg.setAttribute("onclick", "lovd_mapVariants();");
  // -->
</SCRIPT>

</BODY>
</HTML>
"""

ACTA1_VARIANT_DATABASE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>Search unique variants - Leiden Muscular Dystrophy pages - Leiden Open Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
  <META name="Author" content="LOVD development team, LUMC, Netherlands">
  <META name="Generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <LINK rel="stylesheet" type="text/css" href="./styles.css">
  <LINK rel="shortcut icon" href="./favicon.ico">
  <LINK rel="alternate" type="application/atom+xml" title="Leiden Muscular Dystrophy pages Atom 1.0 feed" href="./api/feed.php" />

  <SCRIPT type="text/javascript">
    <!--
    navHome_B     = new Image();
    navHome_B.src = './gfx/tab_home_B.png';
    navHome_H     = new Image();
    navHome_H.src = './gfx/tab_home_H.png';
    navVariants_B     = new Image();
    navVariants_B.src = './gfx/tab_variants_B.png';
    navVariants_H     = new Image();
    navVariants_H.src = './gfx/tab_variants_H.png';
    navSubmitters_B     = new Image();
    navSubmitters_B.src = './gfx/tab_submitters_B.png';
    navSubmitters_H     = new Image();
    navSubmitters_H.src = './gfx/tab_submitters_H.png';
    navSubmit_B     = new Image();
    navSubmit_B.src = './gfx/tab_submit_B.png';
    navSubmit_H     = new Image();
    navSubmit_H.src = './gfx/tab_submit_H.png';
    navDocs_B     = new Image();
    navDocs_B.src = './gfx/tab_docs_B.png';
    navDocs_H     = new Image();
    navDocs_H.src = './gfx/tab_docs_H.png';

    // Used for tab images.
    function lovd_imageSwitch (image_id, image_mode) {
      document.getElementById(image_id).src = eval(image_id + '_' + image_mode + '.src');
    }

    function lovd_switchGeneInline () {
      varForm = '<FORM action="/nmdb2/variants.php" id="SelectGeneDBInline" method="get" style="margin : 0px;"><SELECT name="select_db" onchange="document.getElementById(\'SelectGeneDBInline\').submit();"><OPTION value="ACTA1" selected>ACTA1 (ACTin, Alpha 1 (skeletal muscle))</OPTION><OPTION value="ACTC1">ACTC1 (Actin, alpha, cardiac muscle 1)</OPTION><OPTION value="AGRN">AGRN (Agrin)</OPTION><OPTION value="ANKRD1">ANKRD1 (Ankyrin repeat domain 1 (cardiac muscle))</OPTION><OPTION value="ANO5">ANO5 (Anoctamin 5)</OPTION><OPTION value="ARHGEF10">ARHGEF10 (Rho guanine nucleotide exchange factor (GEF) 10)</OPTION><OPTION value="ASAH1">ASAH1 (N-acylsphingosine amidohydrolase (acid ceramidase) 1)</OPTION><OPTION value="ATL1">ATL1 (Atlastin GTPase 1)</OPTION><OPTION value="B3GALNT2">B3GALNT2 (Beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION><OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION><OPTION value="BAG3">BAG3 (BCL2-associated athanogene 3)</OPTION><OPTION value="BANF1">BANF1 (Barrier to autointegration factor 1)</OPTION><OPTION value="BIN1">BIN1 (Bridging INtegrator 1)</OPTION><OPTION value="BSCL2">BSCL2 (Berardinelli-Seip congenital lipodystrophy 2 (seipin))</OPTION><OPTION value="CAPN3">CAPN3 (Calpain-3)</OPTION><OPTION value="CAV3">CAV3 (Caveolin-3)</OPTION><OPTION value="CCDC78">CCDC78 (Coiled-coil domain containing 78)</OPTION><OPTION value="CCT5">CCT5 (Chaperonin containing TCP1, subunit 5 (epsilon))</OPTION><OPTION value="CFL2">CFL2 (Cofilin 2)</OPTION><OPTION value="CHAT">CHAT (Choline O-acetyltransferase)</OPTION><OPTION value="CHKB">CHKB (Choline kinase beta)</OPTION><OPTION value="CHRNA1">CHRNA1 (cholinergic receptor, nicotinic, alpha 1 (muscle))</OPTION><OPTION value="CHRNB1">CHRNB1 (Cholinergic receptor, nicotinic, beta 1 (muscle))</OPTION><OPTION value="CHRND">CHRND (Cholinergic receptor, nicotinic, delta)</OPTION><OPTION value="CHRNE">CHRNE (Cholinergic receptor, nicotinic, epsilon)</OPTION><OPTION value="CNTN1">CNTN1 (Contactin 1)</OPTION><OPTION value="COL6A1">COL6A1 (Collagen type VI alpha 1)</OPTION><OPTION value="COL6A2">COL6A2 (Collagen type VI alpha 2)</OPTION><OPTION value="COL6A3">COL6A3 (Collagen type VI alpha 3)</OPTION><OPTION value="COLQ">COLQ (Collagen-like tail subunit (single strand of homotrimer) of asymme...))</OPTION><OPTION value="CRYAB">CRYAB (Crystallin, alpha-B)</OPTION><OPTION value="CTDP1">CTDP1 (CTD (carboxy-terminal domain, RNA polymerase II, polypeptide A) p...))</OPTION><OPTION value="DAG1">DAG1 (Dystrophin-Associated Glycoprotein 1)</OPTION><OPTION value="DCTN1">DCTN1 (dynactin 1)</OPTION><OPTION value="DES">DES (Desmin)</OPTION><OPTION value="DMD">DMD (Duchenne Muscular Dystrophy)</OPTION><OPTION value="DMD_d">DMD_d (Duchenne Muscular Dystrophy (whole exon changes))</OPTION><OPTION value="DNAJB6">DNAJB6 (DnaJ (Hsp40) homolog, subfamily B, member 6)</OPTION><OPTION value="DNM2">DNM2 (Dynamin 2)</OPTION><OPTION value="DOK7">DOK7 (Docking protein 7)</OPTION><OPTION value="DPM3">DPM3 (Dolichyl-Phosphate Mannosyltransferase polypeptide 3)</OPTION><OPTION value="DTNA">DTNA (Dystrobrevin alpha)</OPTION><OPTION value="DUX4">DUX4 (Double homeobox 4)</OPTION><OPTION value="DYSF">DYSF (Dysferlin)</OPTION><OPTION value="EGR2">EGR2 (early growth response 2)</OPTION><OPTION value="EMD">EMD (Emery-Dreifuss muscular dystrophy (emerin))</OPTION><OPTION value="FAM134B">FAM134B (family with sequence similarity 134, member B)</OPTION><OPTION value="FGD4">FGD4 (FYVE, RhoGEF and PH domain containing 4)</OPTION><OPTION value="FHL1">FHL1 (Four and a Half LIM domains 1)</OPTION><OPTION value="FIG4">FIG4 (FIG4 homolog, SAC1 lipid phosphatase domain containing (S. cerevis...))</OPTION><OPTION value="FKRP">FKRP (Fukutin-Related Protein)</OPTION><OPTION value="FKTN">FKTN (Fukutin)</OPTION><OPTION value="FLNC">FLNC (Filamin C)</OPTION><OPTION value="GAN">GAN (Gigaxonin)</OPTION><OPTION value="GARS">GARS (glycyl-tRNA synthetase)</OPTION><OPTION value="GDAP1">GDAP1 (ganglioside induced differentiation associated protein 1)</OPTION><OPTION value="GFPT1">GFPT1 (Glutamine-fructose-6-phosphate transaminase 1)</OPTION><OPTION value="GJB1">GJB1 (gap junction protein, beta 1, 32kDa)</OPTION><OPTION value="GK">GK (Glycerol Kinase)</OPTION><OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION><OPTION value="GNB4">GNB4 (Guanine nucleotide binding protein (G protein), beta polypeptide 4)</OPTION><OPTION value="GNE">GNE (glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase)</OPTION><OPTION value="GTDC2">GTDC2 (Glycosyltransferase-like domain containing 2)</OPTION><OPTION value="HSPB1">HSPB1 (heat shock 27kDa protein 1)</OPTION><OPTION value="HSPB3">HSPB3 (heat shock 27kDa protein 3)</OPTION><OPTION value="HSPB8">HSPB8 (heat shock 22kDa protein 8)</OPTION><OPTION value="IGHMBP2">IGHMBP2 (Immunoglobulin mu binding protein 2)</OPTION><OPTION value="IKBKAP">IKBKAP (inhibitor of kappa light polypeptide gene enhancer in B-cells, k...)</OPTION><OPTION value="ISCU">ISCU (Iron-Sulfur cluster scaffold homolog (E. coli))</OPTION><OPTION value="ITGA7">ITGA7 (Integrin, alpha 7)</OPTION><OPTION value="KBTBD13">KBTBD13 (Kelch repeat and BTB (POZ) domain containing 13)</OPTION><OPTION value="KIF1B">KIF1B (kinesin family member 1B)</OPTION><OPTION value="KLHL40">KLHL40 (Kelch-like family member 40)</OPTION><OPTION value="LAMA2">LAMA2 (Laminin-alpha 2 (merosin))</OPTION><OPTION value="LAMP2">LAMP2 (Lysosomal-associated membrane protein 2)</OPTION><OPTION value="LARGE">LARGE (LARGE like-glycosyltransferase)</OPTION><OPTION value="LDB3">LDB3 (LIM domain binding 3 (ZASP))</OPTION><OPTION value="LITAF">LITAF (lipopolysaccharide-induced TNF factor)</OPTION><OPTION value="LMNA">LMNA (Lamin A/C)</OPTION><OPTION value="MATR3">MATR3 (Matrin 3)</OPTION><OPTION value="MFN2">MFN2 (Mitofusin 2)</OPTION><OPTION value="MICU1">MICU1 (Mitochondrial calcium uptake 1)</OPTION><OPTION value="MPZ">MPZ (Myelin protein zero)</OPTION><OPTION value="MSTN">MSTN (Myostatin)</OPTION><OPTION value="MTM1">MTM1 (Myotubularin 1)</OPTION><OPTION value="MTMR14">MTMR14 (Myotubularin related protein 14)</OPTION><OPTION value="MTMR2">MTMR2 (myotubularin related protein 2)</OPTION><OPTION value="MUSK">MUSK (muscle, skeletal, receptor tyrosine kinase)</OPTION><OPTION value="MYBPC3">MYBPC3 (Myosin binding protein C, cardiac)</OPTION><OPTION value="MYH7">MYH7 (myosin, heavy chain 7, cardiac muscle, beta)</OPTION><OPTION value="MYL2">MYL2 (Myosin, light chain 2, regulatory, cardiac, slow)</OPTION><OPTION value="MYL3">MYL3 (Myosin, light chain 3, alkali; ventricular, skeletal, slow)</OPTION><OPTION value="MYOT">MYOT (Myotilin (Titin immunoglobulin domain))</OPTION><OPTION value="MYOZ1">MYOZ1 (Myozenin 1)</OPTION><OPTION value="MYOZ2">MYOZ2 (Myozenin 2)</OPTION><OPTION value="MYOZ3">MYOZ3 (Myozenin 3)</OPTION><OPTION value="MYPN">MYPN (Myopalladin)</OPTION><OPTION value="NDRG1">NDRG1 (N-myc downstream regulated 1)</OPTION><OPTION value="NEB">NEB (Nebulin)</OPTION><OPTION value="NEFL">NEFL (Neurofilament, light polypeptide)</OPTION><OPTION value="NGF">NGF (nerve growth factor (beta polypeptide))</OPTION><OPTION value="NTRK1">NTRK1 (neurotrophic tyrosine kinase, receptor, type 1)</OPTION><OPTION value="PABPN1">PABPN1 (PolyA binding protein, nuclear 1)</OPTION><OPTION value="PDK3">PDK3 (Pyruvate dehydrogenase kinase, isozyme 3)</OPTION><OPTION value="PDLIM3">PDLIM3 (PDZ and LIM domain 3)</OPTION><OPTION value="PLEC">PLEC (Plectin)</OPTION><OPTION value="PLEKHG5">PLEKHG5 (pleckstrin homology domain containing, family G (with RhoGef do...))</OPTION><OPTION value="PMP22">PMP22 (Peripheral myelin protein 22)</OPTION><OPTION value="POMGNT1">POMGNT1 (Protein O-linked Mannose beta1,2-N-acetylGlucosaminylTransferase)</OPTION><OPTION value="POMT1">POMT1 (Protein O-Mannosyltransferase 1)</OPTION><OPTION value="POMT2">POMT2 (Protein O-Mannosyltransferase 2)</OPTION><OPTION value="PRPS1">PRPS1 (phosphoribosyl pyrophosphate synthetase 1)</OPTION><OPTION value="PRX">PRX (periaxin)</OPTION><OPTION value="PTRF">PTRF (Polymerase I and Transcript Release Factor (cavin-1))</OPTION><OPTION value="RAB7A">RAB7A (RAB7A, member RAS oncogene family)</OPTION><OPTION value="RAPSN">RAPSN (Receptor-associated protein of the synapse)</OPTION><OPTION value="RYR1">RYR1 (RYanodine Receptor 1 (skeletal))</OPTION><OPTION value="SBF2">SBF2 (SET binding factor 2)</OPTION><OPTION value="SEPN1">SEPN1 (Selenoprotein 1)</OPTION><OPTION value="SEPT9">SEPT9 (septin 9)</OPTION><OPTION value="SETX">SETX (senataxin)</OPTION><OPTION value="SGCA">SGCA (Sarcoglycan-alpha)</OPTION><OPTION value="SGCB">SGCB (Sarcoglycan-beta)</OPTION><OPTION value="SGCD">SGCD (Sarcoglycan-delta)</OPTION><OPTION value="SGCE">SGCE (Sarcoglycan-epsilon)</OPTION><OPTION value="SGCG">SGCG (Sarcoglycan-gamma)</OPTION><OPTION value="SGCZ">SGCZ (Sarcoglycan-zeta)</OPTION><OPTION value="SH3TC2">SH3TC2 (SH3 domain and tetratricopeptide repeats 2)</OPTION><OPTION value="SLC12A6">SLC12A6 (solute carrier family 12 (potassium/chloride transporters), mem...))</OPTION><OPTION value="SMCHD1">SMCHD1 (Structural maintenance of chromosomes flexible hinge domain cont...)</OPTION><OPTION value="SMN1">SMN1 (Survival Motor Neuron 1)</OPTION><OPTION value="SOX10">SOX10 (SRY (sex determining region Y)-box 10)</OPTION><OPTION value="SPTLC1">SPTLC1 (serine palmitoyltransferase, long chain base subunit 1)</OPTION><OPTION value="SPTLC2">SPTLC2 (serine palmitoyltransferase, long chain base subunit 2)</OPTION><OPTION value="SSPN">SSPN (Sarcospan)</OPTION><OPTION value="SYNE1">SYNE1 (Spectrin repeat containing, Nuclear Envelope 1)</OPTION><OPTION value="SYNE2">SYNE2 (Spectrin repeat containing, Nuclear Envelope 2)</OPTION><OPTION value="TCAP">TCAP (Titin-cap (telethonin))</OPTION><OPTION value="TNNI2">TNNI2 (Troponin I type 2)</OPTION><OPTION value="TNNI3">TNNI3 (Troponin I type 3 (cardiac))</OPTION><OPTION value="TNNT1">TNNT1 (Troponin T type 1)</OPTION><OPTION value="TNNT2">TNNT2 (Troponin T type 2 (cardiac))</OPTION><OPTION value="TNNT3">TNNT3 (Troponin T type 3)</OPTION><OPTION value="TNPO3">TNPO3 (Transportin 3)</OPTION><OPTION value="TPM1">TPM1 (tropomyosin 1 (alpha))</OPTION><OPTION value="TPM2">TPM2 (Tropomyosin 2)</OPTION><OPTION value="TPM3">TPM3 (Tropomyosin 3)</OPTION><OPTION value="TRAPPC11">TRAPPC11 (Trafficking protein particle complex 11)</OPTION><OPTION value="TRDN">TRDN (Triadin)</OPTION><OPTION value="TRIM32">TRIM32 (Tripartite motif-containing 32)</OPTION><OPTION value="TTN">TTN (Titin)</OPTION><OPTION value="TTR">TTR (Transthyretin)</OPTION><OPTION value="VCP">VCP (Valosin-containing protein)</OPTION><OPTION value="VMA21">VMA21 (VMA21 vacuolar H+-ATPase homolog (S. cerevisiae))</OPTION><OPTION value="WNK1">WNK1 (WNK lysine deficient protein kinase 1)</OPTION><OPTION value="YARS">YARS (tyrosyl-tRNA synthetase)</OPTION><OPTION value="ZMPSTE24">ZMPSTE24 (Zinc MetalloPeptidase (STE24 homolog, yeast))</OPTION></SELECT><INPUT type="hidden" name="action" value="search_unique"><INPUT type="submit" value="Switch"></FORM>';
      document.getElementById('gene_name').innerHTML=varForm;
    }

    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="./inc-js-openwindow.php"></SCRIPT>
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD width="150">
      <IMG src="./gfx/LOVD_logo130x50.jpg" alt="LOVD - Leiden Open Variation Database" width="130" height="50">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">Leiden Muscular Dystrophy pages</H2>
      <H5 id="gene_name">ACTin, Alpha 1 (skeletal muscle) (ACTA1)&nbsp;<A href="#" onclick="javascript:lovd_switchGeneInline(); return false;"><IMG src="./gfx/lovd_database_switch_inline.png" width="23" height="23" alt="Switch gene" title="Switch gene database" align="top" border="0"></A></H5>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.2.0 Build 35 [ <A href="./status.php">Current LOVD status</A> ]<BR>
      <A href="./submitters.php?action=register"><B>Register as submitter</B></A> | <A href="./account_login.php"><B>Log in</B></A><BR>
    </TD>
  </TR>
  <TR>
    <TD width="150">&nbsp;</TD>
    <TD valign="top" colspan="2" style="padding-bottom : 2px;"><B>Curators: <A href="mailto:knowak@waimr.uwa.edu.au">Kristen Nowak</A> and <A href="mailto:nlaing@waimr.uwa.edu.au">Nigel Laing</A></B></TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('./gfx/tab_fill.png');">
      <IMG src="./gfx/tab_0B.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/home.php?select_db=ACTA1"><IMG src="./gfx/tab_home_B.png" alt="ACTA1 homepage" title="ACTA1 homepage" width="41" height="30" align="left" id="navHome" border="0" onmouseover="lovd_imageSwitch('navHome', 'H');" onmouseout="lovd_imageSwitch('navHome', 'B');"></A>
      <IMG src="./gfx/tab_BF.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/variants.php?action=search_unique&amp;select_db=ACTA1"><IMG src="./gfx/tab_variants_F.png" alt="View unique variants" title="View unique variants" width="56" height="30" align="left" id="navVariants" border="0"></A>
      <IMG src="./gfx/tab_FB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submitters.php?action=public_list"><IMG src="./gfx/tab_submitters_B.png" alt="Public list of submitters" title="Public list of submitters" width="75" height="30" align="left" id="navSubmitters" border="0" onmouseover="lovd_imageSwitch('navSubmitters', 'H');" onmouseout="lovd_imageSwitch('navSubmitters', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submit.php"><IMG src="./gfx/tab_submit_B.png" alt="Submit new data" title="Submit new data" width="50" height="30" align="left" id="navSubmit" border="0" onmouseover="lovd_imageSwitch('navSubmit', 'H');" onmouseout="lovd_imageSwitch('navSubmit', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/docs/index.php"><IMG src="./gfx/tab_docs_B.png" alt="LOVD manual table of contents" title="LOVD manual table of contents" width="110" height="30" align="left" id="navDocs" border="0" onmouseover="lovd_imageSwitch('navDocs', 'H');" onmouseout="lovd_imageSwitch('navDocs', 'B');"></A>
      <IMG src="./gfx/tab_B0.png" alt="" width="33" height="30" align="left">
    </TD>
  </TR>
</TABLE>

<DIV style="padding : 5px; margin-bottom : 5px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="submenu">
  <TR>
    <TD>
      <TABLE border="0" cellpadding="0" cellspacing="0">
        <TR>
          <TD align="center"><A href="/nmdb2/variants.php?action=view_unique">View&nbsp;unique&nbsp;variants</A></TD>
          <TD style="padding : 0px;">&nbsp;</TD>
          <TD align="center" style="background : #C8DCFA;"><A href="/nmdb2/variants.php?action=search_unique">Search&nbsp;unique&nbsp;variants</A></TD>
          <TD width="1" style="padding : 0px; background : #224488;"><IMG src="./gfx/trans.png" alt="" width="1" height="1"></TD>
          <TD align="center"><A href="/nmdb2/variants.php?action=view_all">View&nbsp;all&nbsp;contents</A></TD>
          <TD style="padding : 0px;">&nbsp;</TD>
          <TD align="center"><A href="/nmdb2/variants.php?action=search_all">Full&nbsp;database&nbsp;search</A></TD>
          <TD width="1" style="padding : 0px; background : #224488;"><IMG src="./gfx/trans.png" alt="" width="1" height="1"></TD>
          <TD align="center"><A href="/nmdb2/variants_overview_origin.php">Variant&nbsp;listing&nbsp;based&nbsp;on&nbsp;patient&nbsp;origin</A></TD>
          <TD width="1" style="padding : 0px; background : #224488;"><IMG src="./gfx/trans.png" alt="" width="1" height="1"></TD>
          <TD align="center"><A href="/nmdb2/variants_statistics.php">Database&nbsp;statistics</A></TD>
          <TD style="padding : 0px;">&nbsp;</TD>
          <TD align="center"><A href="/nmdb2/home.php?action=switch_db">Switch&nbsp;gene</A></TD>
        </TR>
      </TABLE>
    </TD>
  </TR>
</TABLE>
</DIV>




<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD>








      <DIV style="text-align : left;">This is the <b>Laing lab ACTA1 mutation database</b> originally initiated at the <a HREF='http://www.waimr.uwa.edu.au/'>Western Australian Institute for Medical Research (WAIMR)</a>. For purposes of user conveniance it has been combined with other muscle-related gene variant databases at the Leiden Muscular Dystrophy pages.<hr></DIV>

      <IMG src="./gfx/header_variant_listings.png" alt="LOVD - Variant listings for ACTA1" width="500" height="30"><BR>
      <BR>
      <FORM action="/nmdb2/variants.php" method="get" style="margin : 0px;">
        <INPUT type="hidden" name="select_db" value="ACTA1">
        <INPUT type="hidden" name="action" value="search_unique">
        <INPUT type="hidden" name="order" value="Variant/DNA,ASC">
        <INPUT type="hidden" name="hide_col" value="">
        <INPUT type="hidden" name="show_col" value="">

      <SCRIPT type="text/javascript" src="./inc-js-toggle-visibility.js"></SCRIPT>
      <TABLE border="0" cellpadding="0" cellspacing="0" width="960">
        <TR>
          <TD valign="top">
            <TABLE border="0" cellpadding="0" cellspacing="0" class="navigation">
              <TR align="center">
                <TD><A style="color : #999999;">Unhide all columns</A> | <A href="#" onclick="lovd_openWindow('views_columns.php?action=search_unique&amp;hide=true', 'HideColumns', 300, 500); return false;">Hide Specific Columns</A> | <A href="#" onclick="document.forms[0].hide_col.value='all';document.forms[0].submit();">Hide all columns</A></TD></TR></TABLE>

          </TD>
          <TD align="right">
            <TABLE border="0" cellpadding="2" cellspacing="0" width="525" class="info" style="font-size : 11px;">
              <TR>
                <TH>About this overview [<A href="#" id="moreinfo_link" onClick="lovd_toggleVisibility('moreinfo'); return false;">Show</A>]</TH>
              <TR id="moreinfo" style="display : none;">
                <TD>The variants below are all in the ACTA1 database, matching your query. In this view only variant fields are shown. Variants are listed only once, a number is present in the DNA change field when a variant has been reported more than once (in such cases fields other than the DNA change just belong to one entry and may differ for other entries).<BR>Selecting and clicking a specific line will open a detailed view showing all variant entries, including patient and pathogenicity information.<BR>At the bottom of this page a legend is provided with a short explanation of what each field contains.<BR>For a more detailed description of each field, please see the <A href="variants_legend.php?select_db=ACTA1" target="_blank">ACTA1 full legend</A> here.<BR></TD></TR></TABLE></TD></TR></TABLE><BR>

      <SPAN class="S11">232 entries</SPAN><BR>
      <SPAN class="S11"><SELECT name="limit" class="S11" onchange="document.forms[0].submit();">
        <OPTION value="25">25</OPTION>
        <OPTION value="50">50</OPTION>
        <OPTION value="100" selected>100</OPTION>
        <OPTION value="250">250</OPTION>
        <OPTION value="500">500</OPTION>
        <OPTION value="1000">1000</OPTION></SELECT> entries per page</SPAN><BR>

     <DIV id="table_div" style="height : 20px;">
      <TABLE border="0" cellpadding="0" cellspacing="1" class="data" id="table_headers" style="position : absolute; background : #FFFFFF;">
        <TR>
          <TH valign="top" width="20" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Exon,ASC';document.forms[0].submit();">
                <TH>Exon</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Exon column" title="Hide Exon column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Exon';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Exon" value="" title="Exon field should contain..." style="width : 12px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="ordered"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/DNA,DESC';document.forms[0].submit();">
                <TH>DNA&nbsp;change</TH>
                <TD align="right" width="13">&nbsp;</TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc_sel.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/DNA" value="" title="DNA change field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/DNA_published,ASC';document.forms[0].submit();">
                <TH>Var_pub_as</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Var_pub_as column" title="Hide Var_pub_as column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/DNA_published';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/DNA_published" value="" title="Var_pub_as field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="50" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/RNA,ASC';document.forms[0].submit();">
                <TH>RNA&nbsp;change</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide RNA change column" title="Hide RNA change column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/RNA';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/RNA" value="" title="RNA change field should contain..." style="width : 42px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="90" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/DNA_codon,ASC';document.forms[0].submit();">
                <TH>Codon_change</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Codon_change column" title="Hide Codon_change column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/DNA_codon';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/DNA_codon" value="" title="Codon_change field should contain..." style="width : 82px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="60" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Protein,ASC';document.forms[0].submit();">
                <TH>Protein&nbsp;change</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Protein change column" title="Hide Protein change column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Protein';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Protein" value="" title="Protein change field should contain..." style="width : 52px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="60" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/DBID,ASC';document.forms[0].submit();">
                <TH>DB-ID</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide DB-ID column" title="Hide DB-ID column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/DBID';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/DBID" value="" title="DB-ID field should contain..." style="width : 52px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Remarks,ASC';document.forms[0].submit();">
                <TH>Variant&nbsp;remarks</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Variant remarks column" title="Hide Variant remarks column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Remarks';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Remarks" value="" title="Variant remarks field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Genetic_origin,ASC';document.forms[0].submit();">
                <TH>Genet_ori</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Genet_ori column" title="Hide Genet_ori column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Genetic_origin';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Genetic_origin" value="" title="Genet_ori field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Reference,ASC';document.forms[0].submit();">
                <TH>Reference</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Reference column" title="Hide Reference column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Reference';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Reference" value="" title="Reference field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="40" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Detection/Template,ASC';document.forms[0].submit();">
                <TH>Template</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Template column" title="Hide Template column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Detection/Template';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Detection/Template" value="" title="Template field should contain..." style="width : 32px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="40" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Detection/Technique,ASC';document.forms[0].submit();">
                <TH>Technique</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Technique column" title="Hide Technique column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Detection/Technique';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Detection/Technique" value="" title="Technique field should contain..." style="width : 32px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="40" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Frequency,ASC';document.forms[0].submit();">
                <TH>Frequency</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Frequency column" title="Hide Frequency column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Frequency';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Frequency" value="" title="Frequency field should contain..." style="width : 32px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="40" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Restriction_site,ASC';document.forms[0].submit();">
                <TH>RE-site</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide RE-site column" title="Hide RE-site column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Restriction_site';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Restriction_site" value="" title="RE-site field should contain..." style="width : 32px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH></TR></TABLE></DIV>
      <TABLE border="0" cellpadding="0" cellspacing="1" class="data" id="table_data">
        <TR>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.-66_-65delinsTC';">
          <TD width="20">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.-66_-65delinsTC" class="data">c.-66_-65delinsTC</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">-</TD>
          <TD width="60">p.(=)</TD>
          <TD width="60">ACTA1_00200</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.%3D';">
          <TD width="20">1_7</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.%3D" class="data">c.=</A><BR>&nbsp;&nbsp;(Reported 35 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.=</TD>
          <TD width="90">-</TD>
          <TD width="60">p.=</TD>
          <TD width="60">ACTA1_00000</TD>
          <TD width="200">no variants 2nd chromosome</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.7G%3ET';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.7G%3ET" class="data">c.7G>T</A></TD>
          <TD width="200">D1Y</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAC > TAC</TD>
          <TD width="60">p.(Asp3Tyr)</TD>
          <TD width="60">ACTA1_00001</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15520409" target="_blank">Kaindl et al, 2004</A>, <A href="http://www.omim.org/entry/102610#0009" target="_blank">(OMIM 0009)</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.16G%3EA';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.16G%3EA" class="data">c.16G>A</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAG > AAG</TD>
          <TD width="60">p.(Glu6Lys)</TD>
          <TD width="60">ACTA1_00002</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.24C%3EA';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.24C%3EA" class="data">c.24C>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">-</TD>
          <TD width="60">p.(=)</TD>
          <TD width="60">ACTA1_00235</TD>
          <TD width="200">from website <a href='http://genetics.emory.edu/egl/emvclass/emvclass.php'>Emory Genetics Lab</a></TD>
          <TD width="200">unknown</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.37G%3EA';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.37G%3EA" class="data">c.37G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAC > AAC</TD>
          <TD width="60">p.(Asp13Asn)</TD>
          <TD width="60">ACTA1_00160</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.44G%3EA';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.44G%3EA" class="data">c.44G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > GAC</TD>
          <TD width="60">p.(Gly15Asp)</TD>
          <TD width="60">ACTA1_00225</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/20621480" target="_blank"> Stenzel et al 2010</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.49G%3EC';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.49G%3EC" class="data">c.49G>C</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">G15R</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > CGC</TD>
          <TD width="60">p.(Gly17Arg)</TD>
          <TD width="60">ACTA1_00003</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10508519" target="_blank">Nowak et al, 1999</A>, <A href="http://www.omim.org/entry/102610#0003" target="_blank">(OMIM 0003)</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.79G%3EA';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.79G%3EA" class="data">c.79G>A</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAC > AAC</TD>
          <TD width="60">p.(Asp27Asn)</TD>
          <TD width="60">ACTA1_00004</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.89G%3EA';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.89G%3EA" class="data">c.89G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">AGG > AAG</TD>
          <TD width="60">p.(Arg30Lys)</TD>
          <TD width="60">ACTA1_00005</TD>
          <TD width="200">?unaffected father carries the same mutation</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.109G%3EC';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.109G%3EC" class="data">c.109G>C</A><BR>&nbsp;&nbsp;(Reported 7 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTG > CTG</TD>
          <TD width="60">p.(Val37Leu)</TD>
          <TD width="60">ACTA1_00006</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.109G%3ET';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.109G%3ET" class="data">c.109G>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTG > TTG</TD>
          <TD width="60">p.(Val37Leu)</TD>
          <TD width="60">ACTA1_00202</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.110T%3EC';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.110T%3EC" class="data">c.110T>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTG > GCG</TD>
          <TD width="60">p.(Val37Ala)</TD>
          <TD width="60">ACTA1_00161</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.112G%3EA';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.112G%3EA" class="data">c.112G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > AGC</TD>
          <TD width="60">p.(Gly38Ser)</TD>
          <TD width="60">ACTA1_00246</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.113G%3EC';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.113G%3EC" class="data">c.113G>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > GCC</TD>
          <TD width="60">p.(Gly38Ala)</TD>
          <TD width="60">ACTA1_00007</TD>
          <TD width="200">parents not tested</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.119C%3ET';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.119C%3ET" class="data">c.119C>T</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CCC > CTC</TD>
          <TD width="60">p.(Pro40Leu)</TD>
          <TD width="60">ACTA1_00008</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.121C%3ET';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.121C%3ET" class="data">c.121C>T</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CGA > TGA</TD>
          <TD width="60">p.(Arg41*)</TD>
          <TD width="60">ACTA1_00009</TD>
          <TD width="200">both unaffected parents heterozygous</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/17187373" target="_blank">Nowak et al, 2007</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.122G%3EA';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.122G%3EA" class="data">c.122G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CGA > CAA</TD>
          <TD width="60">p.(Arg41Gln)</TD>
          <TD width="60">ACTA1_00229</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">PCR, SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.124C%3ET';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.124C%3ET" class="data">c.124C>T</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CAC > TAC</TD>
          <TD width="60">p.(His42Tyr)</TD>
          <TD width="60">ACTA1_00010</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10508519" target="_blank">Nowak et al, 1999</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.128A%3EG';">
          <TD width="20">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.128A%3EG" class="data">c.128A>G</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CAG > CGG</TD>
          <TD width="60">p.(Gln43Arg)</TD>
          <TD width="60">ACTA1_00011</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/11525890" target="_blank">Wallgren-Pettersson et al, 2001</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15138616" target="_blank">Graziano et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.129%2B31C%3EA';">
          <TD width="20">2i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.129%2B31C%3EA" class="data">c.129+31C>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">-</TD>
          <TD width="60">p.(=)</TD>
          <TD width="60">ACTA1_00236</TD>
          <TD width="200">from website <a href='http://genetics.emory.edu/egl/emvclass/emvclass.php'>Emory Genetics Lab</a></TD>
          <TD width="200">unknown</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.130-10G%3EC';">
          <TD width="20">2i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.130-10G%3EC" class="data">c.130-10G>C</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(=)</TD>
          <TD width="90">-</TD>
          <TD width="60">-</TD>
          <TD width="60">ACTA1_00150</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15138616" target="_blank">Graziano et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.130-5T%3EC';">
          <TD width="20">2i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.130-5T%3EC" class="data">c.130-5T>C</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(=)</TD>
          <TD width="90">-</TD>
          <TD width="60">-</TD>
          <TD width="60">ACTA1_00151</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15138616" target="_blank">Graziano et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.131G%3ET';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.131G%3ET" class="data">c.131G>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > GTC</TD>
          <TD width="60">p.(Gly44Val)</TD>
          <TD width="60">ACTA1_00012</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.133G%3ET';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.133G%3ET" class="data">c.133G>T</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTC > TTC</TD>
          <TD width="60">p.(Val45Phe)</TD>
          <TD width="60">ACTA1_00013</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.137T%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.137T%3EC" class="data">c.137T>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATG > ACG</TD>
          <TD width="60">p.(Met46Thr)</TD>
          <TD width="60">ACTA1_00014</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.142G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.142G%3EA" class="data">c.142G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGT > AGT</TD>
          <TD width="60">p.(Gly48Ser)</TD>
          <TD width="60">ACTA1_00221</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.142G%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.142G%3EC" class="data">c.142G>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGT > CGT</TD>
          <TD width="60">p.(Gly48Arg)</TD>
          <TD width="60">ACTA1_00239</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.142G%3ET';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.142G%3ET" class="data">c.142G>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGT > TGT</TD>
          <TD width="60">p.(Gly48Cys)</TD>
          <TD width="60">ACTA1_00162</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.143G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.143G%3EA" class="data">c.143G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGT > GAT</TD>
          <TD width="60">p.(Gly48Asp)</TD>
          <TD width="60">ACTA1_00015</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.145A%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.145A%3EG" class="data">c.145A>G</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATG > GTG</TD>
          <TD width="60">p.(Met49Val)</TD>
          <TD width="60">ACTA1_00190</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.169G%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.169G%3EC" class="data">c.169G>C</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > CGC</TD>
          <TD width="60">p.(Gly57Arg)</TD>
          <TD width="60">ACTA1_00016</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.172G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.172G%3EA" class="data">c.172G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAC > AAC</TD>
          <TD width="60">p.(Asp58Asn)</TD>
          <TD width="60">ACTA1_00227</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">PCR, SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.197T%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.197T%3EA" class="data">c.197T>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATC > AAC</TD>
          <TD width="60">p.(Ile66Asn)</TD>
          <TD width="60">ACTA1_00212</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.197T%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.197T%3EG" class="data">c.197T>G</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATC > AGC</TD>
          <TD width="60">p.(Ile66Ser)</TD>
          <TD width="60">ACTA1_00163</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.203C%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.203C%3EA" class="data">c.203C>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ACC > AAC</TD>
          <TD width="60">p.(Thr68Asn)</TD>
          <TD width="60">ACTA1_00208</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.203C%3ET';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.203C%3ET" class="data">c.203C>T</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ACC > ATC</TD>
          <TD width="60">p.(Thr68Ile)</TD>
          <TD width="60">ACTA1_00018</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15198992" target="_blank">Ilkovski et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.209A%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.209A%3EG" class="data">c.209A>G</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">AAG > AGG</TD>
          <TD width="60">p.(Lys70Arg)</TD>
          <TD width="60">ACTA1_00186</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.210G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.210G%3EA" class="data">c.210G>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.210g>a</TD>
          <TD width="90">AAG > AAA</TD>
          <TD width="60">p.=</TD>
          <TD width="60">ACTA1_00144</TD>
          <TD width="200">RNA muscle normal; pathogenicity unclear; </TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15138616" target="_blank">Graziano et al, 2004</A></TD>
          <TD width="40">DNA, RNA</TD>
          <TD width="40">RT-PCR, SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.215C%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.215C%3EG" class="data">c.215C>G</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CCT > CGT</TD>
          <TD width="60">p.(Pro72Arg)</TD>
          <TD width="60">ACTA1_00216</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200">unpublished</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.217A%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.217A%3EG" class="data">c.217A>G</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATC > GTC</TD>
          <TD width="60">p.(Ile73Val)</TD>
          <TD width="60">ACTA1_00164</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.217A%3ET';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.217A%3ET" class="data">c.217A>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATC > TTC</TD>
          <TD width="60">p.(Ile73Phe)</TD>
          <TD width="60">ACTA1_00019</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.220G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.220G%3EA" class="data">c.220G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAG > AAG</TD>
          <TD width="60">p.(Glu74Lys)</TD>
          <TD width="60">ACTA1_00020</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15198992" target="_blank">Ilkovski et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.222_223delinsTT';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.222_223delinsTT" class="data">c.222_223delinsTT</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAGCAC > GATTAC</TD>
          <TD width="60">p.(Glu74_His75delinsAspTyr)</TD>
          <TD width="60">ACTA1_00215</TD>
          <TD width="200">GAG CAC > GATTAC</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19553116" target="_blank">Garcia-Angarita, et al 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.223C%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.223C%3EA" class="data">c.223C>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CAC > AAC</TD>
          <TD width="60">p.(His75Asn)</TD>
          <TD width="60">ACTA1_00165</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.224A%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.224A%3EG" class="data">c.224A>G</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CAC > CGC</TD>
          <TD width="60">p.(His75Arg)</TD>
          <TD width="60">ACTA1_00157</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.224A%3ET';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.224A%3ET" class="data">c.224A>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CAC > CTC</TD>
          <TD width="60">p.(His75Leu)</TD>
          <TD width="60">ACTA1_00021</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.227G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.227G%3EA" class="data">c.227G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > GAC</TD>
          <TD width="60">p.(Gly76Asp)</TD>
          <TD width="60">ACTA1_00022</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15952992" target="_blank">Graziano et al, 2005</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.229A%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.229A%3EC" class="data">c.229A>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATC > CTC</TD>
          <TD width="60">p.(Ile77Leu)</TD>
          <TD width="60">ACTA1_00023</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.230T%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.230T%3EG" class="data">c.230T>G</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATC > AGC</TD>
          <TD width="60">p.(Ile77Ser)</TD>
          <TD width="60">ACTA1_00024</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.235A%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.235A%3EG" class="data">c.235A>G</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ACC > GCC</TD>
          <TD width="60">p.(Thr79Ala)</TD>
          <TD width="60">ACTA1_00025</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.253G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.253G%3EA" class="data">c.253G>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAG > AAG</TD>
          <TD width="60">p.(Glu85Lys)</TD>
          <TD width="60">ACTA1_00026</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.275_277del';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.275_277del" class="data">c.275_277del</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">-</TD>
          <TD width="60">p.(Phe92del)</TD>
          <TD width="60">ACTA1_00231</TD>
          <TD width="200">deleted sequence = TCT</TD>
          <TD width="200">de novo</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.282C%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.282C%3EG" class="data">c.282C>G</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">AAC > AAG</TD>
          <TD width="60">p.(Asn94Lys)</TD>
          <TD width="60">ACTA1_00027</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.287T%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.287T%3EC" class="data">c.287T>C</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">Leu94Pro</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CTT > CCT</TD>
          <TD width="60">p.(Leu96Pro)</TD>
          <TD width="60">ACTA1_00210</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10508519" target="_blank">Nowak et al, 1999</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.omim.org/entry/102610#0001" target="_blank">(OMIM 0001)</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.324C%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.324C%3EA" class="data">c.324C>A</A></TD>
          <TD width="200">Thr108Thr</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ACC > ACA</TD>
          <TD width="60">p.(=)</TD>
          <TD width="60">ACTA1_00196</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?type=rs&rs=rs41271479" target="_blank">dbSNP-rs41271479</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">?</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.327G%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.327G%3EC" class="data">c.327G>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAG > GAC</TD>
          <TD width="60">p.(Glu109Asp)</TD>
          <TD width="60">ACTA1_00029</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.338A%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.338A%3EG" class="data">c.338A>G</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">AAT > AGT</TD>
          <TD width="60">p.(Asn113Ser)</TD>
          <TD width="60">ACTA1_00030</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.343A%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.343A%3EG" class="data">c.343A>G</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">AAG > GAG</TD>
          <TD width="60">p.(Lys115Glu)</TD>
          <TD width="60">ACTA1_00166</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.346G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.346G%3EA" class="data">c.346G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GCC > ACC</TD>
          <TD width="60">p.(Ala116Thr)</TD>
          <TD width="60">ACTA1_00031</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.346G%3ET';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.346G%3ET" class="data">c.346G>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GCC > TCC</TD>
          <TD width="60">p.(Ala116Ser)</TD>
          <TD width="60">ACTA1_00032</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.350A%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.350A%3EC" class="data">c.350A>C</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">AAC > ACC</TD>
          <TD width="60">p.(Asn117Thr)</TD>
          <TD width="60">ACTA1_00034</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.350A%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.350A%3EG" class="data">c.350A>G</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">N115S</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">AAC > AGC</TD>
          <TD width="60">p.(Asn117Ser)</TD>
          <TD width="60">ACTA1_00033</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10508519" target="_blank">Nowak et al, 1999</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/11333380" target="_blank">Ilkovski et al, 2001</A>, <A href="http://www.omim.org/entry/102610#0002" target="_blank">(OMIM 0002)</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.353G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.353G%3EA" class="data">c.353G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CGC > CAC</TD>
          <TD width="60">p.(Arg118His)</TD>
          <TD width="60">ACTA1_00035</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.360G%3ET';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.360G%3ET" class="data">c.360G>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">AAG > AAT</TD>
          <TD width="60">p.(Lys120Asn)</TD>
          <TD width="60">ACTA1_00219</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">PCR, SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.365C%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.365C%3EG" class="data">c.365C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ACC > AGC</TD>
          <TD width="60">p.(Thr122Ser)</TD>
          <TD width="60">ACTA1_00036</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.393delG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.393delG" class="data">c.393delG</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTG > GTC</TD>
          <TD width="60">p.(Ala133Profs*59)</TD>
          <TD width="60">ACTA1_00037</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.400A%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.400A%3EG" class="data">c.400A>G</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATG > GTG</TD>
          <TD width="60">p.(Met134Val)</TD>
          <TD width="60">ACTA1_00038</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10508519" target="_blank">Nowak et al, 1999</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/11166164" target="_blank">Junglbuth et al, 2001</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.402G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.402G%3EA" class="data">c.402G>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATG > ATA</TD>
          <TD width="60">p.(Met134Ile)</TD>
          <TD width="60">ACTA1_00039</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.407T%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.407T%3EC" class="data">c.407T>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTG > GCG</TD>
          <TD width="60">p.(Val136Ala)</TD>
          <TD width="60">ACTA1_00040</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.413T%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.413T%3EC" class="data">c.413T>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATC > ACC</TD>
          <TD width="60">p.(Ile138Thr)</TD>
          <TD width="60">ACTA1_00042</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.414C%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.414C%3EG" class="data">c.414C>G</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">I136M</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ATC > ATG</TD>
          <TD width="60">p.(Ile138Met)</TD>
          <TD width="60">ACTA1_00041</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10838259" target="_blank">Schnell et al, 2000</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/11333380" target="_blank">Ilkovski et al, 2001</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.omim.org/entry/102610#0008" target="_blank">(OMIM 0008)</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.417G%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.417G%3EC" class="data">c.417G>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CAG > CAC</TD>
          <TD width="60">p.(Gln139His)</TD>
          <TD width="60">ACTA1_00043</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/18461503" target="_blank">Koy et al, 2007</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.418G%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.418G%3EC" class="data">c.418G>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GCC > CCC</TD>
          <TD width="60">p.(Ala140Pro)</TD>
          <TD width="60">ACTA1_00044</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.419C%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.419C%3EA" class="data">c.419C>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GCC > GAC</TD>
          <TD width="60">p.(Ala140Asp)</TD>
          <TD width="60">ACTA1_00195</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.422T%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.422T%3EC" class="data">c.422T>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTG > GCG</TD>
          <TD width="60">p.(Val141Ala)</TD>
          <TD width="60">ACTA1_00045</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.425T%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.425T%3EC" class="data">c.425T>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CTG > CCG</TD>
          <TD width="60">p.(Leu142Pro)</TD>
          <TD width="60">ACTA1_00046</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.430C%3ET';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.430C%3ET" class="data">c.430C>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CTC > TTC</TD>
          <TD width="60">p.(Leu144Phe)</TD>
          <TD width="60">ACTA1_00197</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19553121" target="_blank">Arai et al, 2009</A>  <A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.435C%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.435C%3EG" class="data">c.435C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">TAC > TAG</TD>
          <TD width="60">p.(Tyr145*)</TD>
          <TD width="60">ACTA1_00184</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.436delG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.436delG" class="data">c.436delG</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">-</TD>
          <TD width="60">p.(Ala146Profs*46)</TD>
          <TD width="60">ACTA1_00047</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/11525890" target="_blank">Wallgren-Pettersson et al, 2001</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.437_442dup';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.437_442dup" class="data">c.437_442dup</A></TD>
          <TD width="200">436_441dup</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">-</TD>
          <TD width="60">p.(Ala146_Ser147dup)</TD>
          <TD width="60">ACTA1_00048</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.442G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.442G%3EA" class="data">c.442G>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > AGC</TD>
          <TD width="60">p.(Gly148Ser)</TD>
          <TD width="60">ACTA1_00050</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.443G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.443G%3EA" class="data">c.443G>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > GAC</TD>
          <TD width="60">p.(Gly148Asp)</TD>
          <TD width="60">ACTA1_00049</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15236405" target="_blank">Agrawal et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.446G%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.446G%3EA" class="data">c.446G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">AGG > AAG</TD>
          <TD width="60">p.(Arg149Lys)</TD>
          <TD width="60">ACTA1_00051</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.449C%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.449C%3EA" class="data">c.449C>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ACC > AAC</TD>
          <TD width="60">p.(Thr150Asn)</TD>
          <TD width="60">ACTA1_00052</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.449C%3EG';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.449C%3EG" class="data">c.449C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ACC > AGC</TD>
          <TD width="60">p.(Thr150Ser)</TD>
          <TD width="60">ACTA1_00053</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.453C%3EA';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.453C%3EA" class="data">c.453C>A</A></TD>
          <TD width="200">Thr151Thr</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">ACC > ACA</TD>
          <TD width="60">p.(=)</TD>
          <TD width="60">ACTA1_00145</TD>
          <TD width="200">known polymorphism</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10528865" target="_blank">Mayosi et al, 1999</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.454%2B30CCCGCC%283_5%29';">
          <TD width="20">3i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.454%2B30CCCGCC%283_5%29" class="data">c.454+30CCCGCC(3_5)</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(=)</TD>
          <TD width="90">-</TD>
          <TD width="60">p.(=)</TD>
          <TD width="60">ACTA1_00152</TD>
          <TD width="200">known polymorphism</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10508519" target="_blank">Nowak et al, 1999</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15138616" target="_blank">Graziano et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.455-53A%3EC';">
          <TD width="20">3i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.455-53A%3EC" class="data">c.455-53A>C</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">455-53C>A</TD>
          <TD width="50">r.(=)</TD>
          <TD width="90">-</TD>
          <TD width="60">-</TD>
          <TD width="60">ACTA1_00193</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.455-1G%3EA';">
          <TD width="20">3i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.455-1G%3EA" class="data">c.455-1G>A</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.spl?</TD>
          <TD width="90">-</TD>
          <TD width="60">-</TD>
          <TD width="60">ACTA1_00139</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.460G%3EC';">
          <TD width="20">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.460G%3EC" class="data">c.460G>C</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">-</TD>
          <TD width="60">p.(Val154Leu)</TD>
          <TD width="60">ACTA1_00245</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ, SEQ-NG</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.455G%3EC';">
          <TD width="20">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.455G%3EC" class="data">c.455G>C</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGC > GCC</TD>
          <TD width="60">p.(Gly152Ala)</TD>
          <TD width="60">ACTA1_00217</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/[20850316]" target="_blank">[Ravenscroft et al 2011]</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.466G%3EA';">
          <TD width="20">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.466G%3EA" class="data">c.466G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GAC > AAC</TD>
          <TD width="60">p.(Asp156Asn)</TD>
          <TD width="60">ACTA1_00054</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15221331" target="_blank">Schroder et al, 2004</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.478G%3ET';">
          <TD width="20">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.478G%3ET" class="data">c.478G>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GGT > TGT</TD>
          <TD width="60">p.(Gly160Cys)</TD>
          <TD width="60">ACTA1_00187</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.487C%3EG';">
          <TD width="20">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.487C%3EG" class="data">c.487C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CAC > GAC</TD>
          <TD width="60">p.(His163Asp)</TD>
          <TD width="60">ACTA1_00055</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.487C%3ET';">
          <TD width="20">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.487C%3ET" class="data">c.487C>T</A></TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">CAC > TAC</TD>
          <TD width="60">p.(His163Tyr)</TD>
          <TD width="60">ACTA1_00218</TD>
          <TD width="200">?recessive variant</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.493G%3EA';">
          <TD width="20">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.493G%3EA" class="data">c.493G>A</A></TD>
          <TD width="200">V163M</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTG > ATG</TD>
          <TD width="60">p.(Val165Met)</TD>
          <TD width="60">ACTA1_00058</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/15198992" target="_blank">Ilkovski et al, 2004</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/16427282" target="_blank">Hutchinson et al, 2006</A>, <A href="http://www.omim.org/entry/102610#0014" target="_blank">(OMIM 0014)</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.493G%3EC';">
          <TD width="20">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.493G%3EC" class="data">c.493G>C</A></TD>
          <TD width="200">V163L</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTG > CTG</TD>
          <TD width="60">p.(Val165Leu)</TD>
          <TD width="60">ACTA1_00056</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10508519" target="_blank">Nowak et al, 1999</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.omim.org/entry/102610#0004" target="_blank">(OMIM 0004)</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.493G%3ET';">
          <TD width="20">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.493G%3ET" class="data">c.493G>T</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">V163L</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GTG > TTG</TD>
          <TD width="60">p.(Val165Leu)</TD>
          <TD width="60">ACTA1_00057</TD>
          <TD width="200">-</TD>
          <TD width="200">germline (inherited)</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10508519" target="_blank">Nowak et al, 1999</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/12921789" target="_blank">Sparrow et al, 2003</A>, <A href="http://www.omim.org/entry/102610#0004" target="_blank">(OMIM 0004)</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.515C%3EA';">
          <TD width="20">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=ACTA1&amp;action=search_all&amp;search_Variant%2FDNA=c.515C%3EA" class="data">c.515C>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="50">r.(?)</TD>
          <TD width="90">GCG > GAG</TD>
          <TD width="60">p.(Ala172Glu)</TD>
          <TD width="60">ACTA1_00059</TD>
          <TD width="200">-</TD>
          <TD width="200">de novo</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/19562689" target="_blank">Laing et al, 2009</A></TD>
          <TD width="40">DNA</TD>
          <TD width="40">SEQ</TD>
          <TD width="40">-</TD>
          <TD width="40">-</TD></TR></TABLE>
</FORM>

      <SPAN class="S11">
      1 - 100
      <BR>
 [&lt;-]  <B>1</B>  <A href="/nmdb2/variants.php?action=search_unique&amp;limit=100&amp;order=Variant%2FDNA%2CASC&amp;page=2">2</A>  <A href="/nmdb2/variants.php?action=search_unique&amp;limit=100&amp;order=Variant%2FDNA%2CASC&amp;page=3">3</A>  [<A href="/nmdb2/variants.php?action=search_unique&amp;limit=100&amp;order=Variant%2FDNA%2CASC&amp;page=2">-&gt;</A>]      </SPAN><BR>
      <BR>

This is the <b>Laing lab ACTA1 mutation database</b> originally initiated at the <a HREF='http://www.waimr.uwa.edu.au/'>Western Australian Institute for Medical Research (WAIMR)</a>. For purposes of user conveniance it has been combined with other muscle-related gene variant databases at the Leiden Muscular Dystrophy pages.<hr><BR><BR>

      <SPAN class="S15"><B>Legend:</B></SPAN> [ <A href="variants_legend.php?select_db=ACTA1" target="_blank">ACTA1 full legend</A> ]<BR>

      <SPAN class="S11">
        Sequence variations are described basically as recommended by the Ad-Hoc Committee for Mutation Nomenclature (AHCMN), with the recently suggested additions (den Dunnen JT and Antonarakis SE [2000], Hum.Mut. 15:7-12); for a summary see <A href="http://www.HGVS.org/mutnomen/"><B>Nomenclature</B></A>.
        <A href="http://www.dmd.nl/nmdb2/refseq/ACTA1_codingDNA.html">Coding DNA Reference Sequence</A>, with the first base of the Met-codon counted as position 1.<BR>
        <B>Exon:</B> number of exon/intron containing variant <B>DNA change:</B> DNA change <B>Var_pub_as:</B> Var_pub_as <B>RNA change:</B> RNA change <B>Codon_change:</B> DNA_codon <B>Protein change:</B> Protein change <B>ACTA1 DB-ID:</B> DB-ID <B>Variant remarks:</B> Variant remarks <B>Genet_ori:</B> origin of variant; unknown, germline (i.e. inherited), somatic, de novo, from parental disomy (maternal or paternal) or in vitro (cloned) <B>Reference:</B> publication describing the variant submitted, incl. links to OMIM and dbSNP (when available) <B>Template:</B> Template <B>Technique:</B> Technique <B>Frequency:</B> Frequency <B>RE-site:</B> RE-site</SPAN><BR><BR>









    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/2.0/" target="_blank">LOVD v.2.0</A> Build 35<BR>
  Enabled modules: recaptcha, showmaxdbid, mutalyzer<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_update_newest_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>

<SCRIPT type="text/javascript">
  <!--
  objImg = document.getElementById('mapping_progress');

function lovd_HTTPRequest (sURL) {
    // Create HTTP request object.
    var objHTTP;
    try {
        // W3C standard.
        objHTTP = new XMLHttpRequest();
    } catch (e) {
        // Internet Explorer?
        try {
            objHTTP = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                objHTTP = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
                // Ok, last try!
                try {
                    objHTTP = window.createRequest();
                } catch (e) {
                    // Never mind.
                    objHTTP = false;
                }
            }
        }
    }

    if (objHTTP) {
        objHTTP.open("GET", sURL, false);
        objHTTP.send(null);
        return objHTTP;

    } else {
        return false;
    }
}



  function lovd_mapVariants () {
    // Request file that will do the actual work.
    objHTTP = lovd_HTTPRequest("http://www.dmd.nl/nmdb2/ajax-map_variants.php");

    if (!objHTTP || objHTTP.status != 200) {
        // Don't try again.
        objImg.src = "./gfx/lovd_mapping_99.png";
        objImg.title = "There was a problem with LOVD while mapping variants to the genome.";
    } else {
        aResponse = objHTTP.responseText.split("\t");
        // 2010-05-03; 2.0-26; Verify output, to prevent PHP errors from freaking out the browser (= every 50 microseconds a new request).
        // Took (and shortened) the "is_numeric()" implementation from http://phpjs.org/functions/is_numeric:449 (thanks guys).
        if (aResponse.length == 2 && !isNaN(aResponse[0])) {
            objImg.src = "./gfx/lovd_mapping_" + aResponse[0] + ".png";
            objImg.title = aResponse[1];

            if (aResponse[1] != "All done!") {
                setTimeout("lovd_mapVariants()", 50);
            } else {
                objImg.setAttribute("onclick", "lovd_mapVariants();");
            }
        } else {
            objImg.title = "Error occured: " + objHTTP.responseText;
        }
    }
  }

objImg.setAttribute("onclick", "lovd_mapVariants();");
  // -->
</SCRIPT>

<SCRIPT type="text/javascript" src="./inc-js-sticky_header.js"></SCRIPT>
</BODY></HTML>"""

ACTA1_TABLE_DATA = [['1', 'NM_001100.3:c.-66_-65delinsTC', '-', 'r.(?)', '-', 'p.(=)', 'ACTA1_00200', '-', 'germline (inherited)', '-', 'DNA', 'SEQ', '-', '-'], ['1_7', 'NM_001100.3:c.=', '-', 'r.=', '-', 'p.=', 'ACTA1_00000', 'no variants 2nd chromosome', 'germline (inherited)', '-', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.7G>T', 'D1Y', 'r.(?)', 'GAC > TAC', 'p.(Asp3Tyr)', 'ACTA1_00001', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15520409,http://www.omim.org/entry/102610#0009', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.16G>A', '-', 'r.(?)', 'GAG > AAG', 'p.(Glu6Lys)', 'ACTA1_00002', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.24C>A', '-', 'r.(?)', '-', 'p.(=)', 'ACTA1_00235', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.37G>A', '-', 'r.(?)', 'GAC > AAC', 'p.(Asp13Asn)', 'ACTA1_00160', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.44G>A', '-', 'r.(?)', 'GGC > GAC', 'p.(Gly15Asp)', 'ACTA1_00225', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/20621480', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.49G>C', 'G15R', 'r.(?)', 'GGC > CGC', 'p.(Gly17Arg)', 'ACTA1_00003', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.omim.org/entry/102610#0003', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.79G>A', '-', 'r.(?)', 'GAC > AAC', 'p.(Asp27Asn)', 'ACTA1_00004', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.89G>A', '-', 'r.(?)', 'AGG > AAG', 'p.(Arg30Lys)', 'ACTA1_00005', '?unaffected father carries the same mutation', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.109G>C', '-', 'r.(?)', 'GTG > CTG', 'p.(Val37Leu)', 'ACTA1_00006', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.109G>T', '-', 'r.(?)', 'GTG > TTG', 'p.(Val37Leu)', 'ACTA1_00202', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.110T>C', '-', 'r.(?)', 'GTG > GCG', 'p.(Val37Ala)', 'ACTA1_00161', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.112G>A', '-', 'r.(?)', 'GGC > AGC', 'p.(Gly38Ser)', 'ACTA1_00246', '-', 'de novo', '-', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.113G>C', '-', 'r.(?)', 'GGC > GCC', 'p.(Gly38Ala)', 'ACTA1_00007', 'parents not tested', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.119C>T', '-', 'r.(?)', 'CCC > CTC', 'p.(Pro40Leu)', 'ACTA1_00008', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.121C>T', '-', 'r.(?)', 'CGA > TGA', 'p.(Arg41*)', 'ACTA1_00009', 'both unaffected parents heterozygous', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/17187373,http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.122G>A', '-', 'r.(?)', 'CGA > CAA', 'p.(Arg41Gln)', 'ACTA1_00229', '-', 'de novo', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['2', 'NM_001100.3:c.124C>T', '-', 'r.(?)', 'CAC > TAC', 'p.(His42Tyr)', 'ACTA1_00010', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_001100.3:c.128A>G', '-', 'r.(?)', 'CAG > CGG', 'p.(Gln43Arg)', 'ACTA1_00011', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/11525890,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['2i', 'NM_001100.3:c.129+31C>A', '-', 'r.(?)', '-', 'p.(=)', 'ACTA1_00236', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['2i', 'NM_001100.3:c.130-10G>C', '-', 'r.(=)', '-', '-', 'ACTA1_00150', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['2i', 'NM_001100.3:c.130-5T>C', '-', 'r.(=)', '-', '-', 'ACTA1_00151', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.131G>T', '-', 'r.(?)', 'GGC > GTC', 'p.(Gly44Val)', 'ACTA1_00012', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.133G>T', '-', 'r.(?)', 'GTC > TTC', 'p.(Val45Phe)', 'ACTA1_00013', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.137T>C', '-', 'r.(?)', 'ATG > ACG', 'p.(Met46Thr)', 'ACTA1_00014', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.142G>A', '-', 'r.(?)', 'GGT > AGT', 'p.(Gly48Ser)', 'ACTA1_00221', '-', 'germline (inherited)', '-', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.142G>C', '-', 'r.(?)', 'GGT > CGT', 'p.(Gly48Arg)', 'ACTA1_00239', '-', 'de novo', '-', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.142G>T', '-', 'r.(?)', 'GGT > TGT', 'p.(Gly48Cys)', 'ACTA1_00162', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.143G>A', '-', 'r.(?)', 'GGT > GAT', 'p.(Gly48Asp)', 'ACTA1_00015', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.145A>G', '-', 'r.(?)', 'ATG > GTG', 'p.(Met49Val)', 'ACTA1_00190', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.169G>C', '-', 'r.(?)', 'GGC > CGC', 'p.(Gly57Arg)', 'ACTA1_00016', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.172G>A', '-', 'r.(?)', 'GAC > AAC', 'p.(Asp58Asn)', 'ACTA1_00227', '-', 'germline (inherited)', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['3', 'NM_001100.3:c.197T>A', '-', 'r.(?)', 'ATC > AAC', 'p.(Ile66Asn)', 'ACTA1_00212', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.197T>G', '-', 'r.(?)', 'ATC > AGC', 'p.(Ile66Ser)', 'ACTA1_00163', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.203C>A', '-', 'r.(?)', 'ACC > AAC', 'p.(Thr68Asn)', 'ACTA1_00208', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.203C>T', '-', 'r.(?)', 'ACC > ATC', 'p.(Thr68Ile)', 'ACTA1_00018', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/15198992', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.209A>G', '-', 'r.(?)', 'AAG > AGG', 'p.(Lys70Arg)', 'ACTA1_00186', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.210G>A', '-', 'r.210g>a', 'AAG > AAA', 'p.=', 'ACTA1_00144', 'RNA muscle normal; pathogenicity unclear;', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['3', 'NM_001100.3:c.215C>G', '-', 'r.(?)', 'CCT > CGT', 'p.(Pro72Arg)', 'ACTA1_00216', '-', 'germline (inherited)', 'unpublished', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.217A>G', '-', 'r.(?)', 'ATC > GTC', 'p.(Ile73Val)', 'ACTA1_00164', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.217A>T', '-', 'r.(?)', 'ATC > TTC', 'p.(Ile73Phe)', 'ACTA1_00019', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.220G>A', '-', 'r.(?)', 'GAG > AAG', 'p.(Glu74Lys)', 'ACTA1_00020', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/15198992', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.222_223delinsTT', '-', 'r.(?)', 'GAGCAC > GATTAC', 'p.(Glu74_His75delinsAspTyr)', 'ACTA1_00215', 'GAG CAC > GATTAC', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19553116', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.223C>A', '-', 'r.(?)', 'CAC > AAC', 'p.(His75Asn)', 'ACTA1_00165', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.224A>G', '-', 'r.(?)', 'CAC > CGC', 'p.(His75Arg)', 'ACTA1_00157', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.224A>T', '-', 'r.(?)', 'CAC > CTC', 'p.(His75Leu)', 'ACTA1_00021', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.227G>A', '-', 'r.(?)', 'GGC > GAC', 'p.(Gly76Asp)', 'ACTA1_00022', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/15952992', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.229A>C', '-', 'r.(?)', 'ATC > CTC', 'p.(Ile77Leu)', 'ACTA1_00023', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.230T>G', '-', 'r.(?)', 'ATC > AGC', 'p.(Ile77Ser)', 'ACTA1_00024', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.235A>G', '-', 'r.(?)', 'ACC > GCC', 'p.(Thr79Ala)', 'ACTA1_00025', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.253G>A', '-', 'r.(?)', 'GAG > AAG', 'p.(Glu85Lys)', 'ACTA1_00026', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.275_277del', '-', 'r.(?)', '-', 'p.(Phe92del)', 'ACTA1_00231', 'deleted sequence = TCT', 'de novo', '-', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.282C>G', '-', 'r.(?)', 'AAC > AAG', 'p.(Asn94Lys)', 'ACTA1_00027', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.287T>C', 'Leu94Pro', 'r.(?)', 'CTT > CCT', 'p.(Leu96Pro)', 'ACTA1_00210', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.omim.org/entry/102610#0001', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.324C>A', 'Thr108Thr', 'r.(?)', 'ACC > ACA', 'p.(=)', 'ACTA1_00196', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?type=rs&rs=rs41271479', 'DNA', 'SEQ', '?', '-'], ['3', 'NM_001100.3:c.327G>C', '-', 'r.(?)', 'GAG > GAC', 'p.(Glu109Asp)', 'ACTA1_00029', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.338A>G', '-', 'r.(?)', 'AAT > AGT', 'p.(Asn113Ser)', 'ACTA1_00030', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.343A>G', '-', 'r.(?)', 'AAG > GAG', 'p.(Lys115Glu)', 'ACTA1_00166', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.346G>A', '-', 'r.(?)', 'GCC > ACC', 'p.(Ala116Thr)', 'ACTA1_00031', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.346G>T', '-', 'r.(?)', 'GCC > TCC', 'p.(Ala116Ser)', 'ACTA1_00032', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.350A>C', '-', 'r.(?)', 'AAC > ACC', 'p.(Asn117Thr)', 'ACTA1_00034', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.350A>G', 'N115S', 'r.(?)', 'AAC > AGC', 'p.(Asn117Ser)', 'ACTA1_00033', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/11333380,http://www.omim.org/entry/102610#0002', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.353G>A', '-', 'r.(?)', 'CGC > CAC', 'p.(Arg118His)', 'ACTA1_00035', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.360G>T', '-', 'r.(?)', 'AAG > AAT', 'p.(Lys120Asn)', 'ACTA1_00219', '-', 'de novo', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['3', 'NM_001100.3:c.365C>G', '-', 'r.(?)', 'ACC > AGC', 'p.(Thr122Ser)', 'ACTA1_00036', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.393delG', '-', 'r.(?)', 'GTG > GTC', 'p.(Ala133Profs*59)', 'ACTA1_00037', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.400A>G', '-', 'r.(?)', 'ATG > GTG', 'p.(Met134Val)', 'ACTA1_00038', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/11166164,http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.402G>A', '-', 'r.(?)', 'ATG > ATA', 'p.(Met134Ile)', 'ACTA1_00039', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.407T>C', '-', 'r.(?)', 'GTG > GCG', 'p.(Val136Ala)', 'ACTA1_00040', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.413T>C', '-', 'r.(?)', 'ATC > ACC', 'p.(Ile138Thr)', 'ACTA1_00042', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.414C>G', 'I136M', 'r.(?)', 'ATC > ATG', 'p.(Ile138Met)', 'ACTA1_00041', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10838259,http://www.ncbi.nlm.nih.gov/pubmed/11333380,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.omim.org/entry/102610#0008', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.417G>C', '-', 'r.(?)', 'CAG > CAC', 'p.(Gln139His)', 'ACTA1_00043', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/18461503', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.418G>C', '-', 'r.(?)', 'GCC > CCC', 'p.(Ala140Pro)', 'ACTA1_00044', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.419C>A', '-', 'r.(?)', 'GCC > GAC', 'p.(Ala140Asp)', 'ACTA1_00195', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.422T>C', '-', 'r.(?)', 'GTG > GCG', 'p.(Val141Ala)', 'ACTA1_00045', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.425T>C', '-', 'r.(?)', 'CTG > CCG', 'p.(Leu142Pro)', 'ACTA1_00046', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.430C>T', '-', 'r.(?)', 'CTC > TTC', 'p.(Leu144Phe)', 'ACTA1_00197', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19553121,http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.435C>G', '-', 'r.(?)', 'TAC > TAG', 'p.(Tyr145*)', 'ACTA1_00184', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.436delG', '-', 'r.(?)', '-', 'p.(Ala146Profs*46)', 'ACTA1_00047', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/11525890,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.437_442dup', '436_441dup', 'r.(?)', '-', 'p.(Ala146_Ser147dup)', 'ACTA1_00048', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.442G>A', '-', 'r.(?)', 'GGC > AGC', 'p.(Gly148Ser)', 'ACTA1_00050', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.443G>A', '-', 'r.(?)', 'GGC > GAC', 'p.(Gly148Asp)', 'ACTA1_00049', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.446G>A', '-', 'r.(?)', 'AGG > AAG', 'p.(Arg149Lys)', 'ACTA1_00051', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.449C>A', '-', 'r.(?)', 'ACC > AAC', 'p.(Thr150Asn)', 'ACTA1_00052', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.449C>G', '-', 'r.(?)', 'ACC > AGC', 'p.(Thr150Ser)', 'ACTA1_00053', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.453C>A', 'Thr151Thr', 'r.(?)', 'ACC > ACA', 'p.(=)', 'ACTA1_00145', 'known polymorphism', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10528865', 'DNA', 'SEQ', '-', '-'], ['3i', 'NM_001100.3:c.454+30CCCGCC(3_5)', '-', 'r.(=)', '-', 'p.(=)', 'ACTA1_00152', 'known polymorphism', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['3i', 'NM_001100.3:c.455-53A>C', '455-53C>A', 'r.(=)', '-', '-', 'ACTA1_00193', '-', 'germline (inherited)', '-', 'DNA', 'SEQ', '-', '-'], ['3i', 'NM_001100.3:c.455-1G>A', '-', 'r.spl?', '-', '-', 'ACTA1_00139', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_001100.3:c.460G>C', '-', 'r.(?)', '-', 'p.(Val154Leu)', 'ACTA1_00245', '-', 'germline (inherited)', '-', 'DNA', 'SEQ, SEQ-NG', '-', '-'], ['4', 'NM_001100.3:c.455G>C', '-', 'r.(?)', 'GGC > GCC', 'p.(Gly152Ala)', 'ACTA1_00217', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/[20850316]', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.466G>A', '-', 'r.(?)', 'GAC > AAC', 'p.(Asp156Asn)', 'ACTA1_00054', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15221331', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.478G>T', '-', 'r.(?)', 'GGT > TGT', 'p.(Gly160Cys)', 'ACTA1_00187', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.487C>G', '-', 'r.(?)', 'CAC > GAC', 'p.(His163Asp)', 'ACTA1_00055', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.487C>T', '-', 'r.(?)', 'CAC > TAC', 'p.(His163Tyr)', 'ACTA1_00218', '?recessive variant', 'germline (inherited)', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.493G>A', 'V163M', 'r.(?)', 'GTG > ATG', 'p.(Val165Met)', 'ACTA1_00058', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15198992,http://www.ncbi.nlm.nih.gov/pubmed/16427282,http://www.omim.org/entry/102610#0014', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.493G>C', 'V163L', 'r.(?)', 'GTG > CTG', 'p.(Val165Leu)', 'ACTA1_00056', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.omim.org/entry/102610#0004', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.493G>T', 'V163L', 'r.(?)', 'GTG > TTG', 'p.(Val165Leu)', 'ACTA1_00057', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.omim.org/entry/102610#0004', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.515C>A', '-', 'r.(?)', 'GCG > GAG', 'p.(Ala172Glu)', 'ACTA1_00059', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.515C>G', '-', 'r.(?)', 'GCG > GGG', 'p.(Ala172Gly)', 'ACTA1_00060', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.539T>C', '-', 'r.(?)', 'CTG > CCG', 'p.(Leu180Pro)', 'ACTA1_00061', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.541delG', '-', 'r.(?)', '-', 'p.(Asp181Thrfs*11)', 'ACTA1_00066', 'both parents carriers', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/17187373', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.541G>A', '-', 'r.(?)', 'GAC > AAC', 'p.(Asp181Asn)', 'ACTA1_00062', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.541G>C', '-', 'r.(?)', 'GAC > CAC', 'p.(Asp181His)', 'ACTA1_00063', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.542A>G', '-', 'r.(?)', 'GAC > GGC', 'p.(Asp181Gly)', 'ACTA1_00064', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.547G>A', '-', 'r.(?)', 'GCG > ACG', 'p.(Ala183Thr)', 'ACTA1_00168', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.549G>A', 'Ala183Ala', 'r.(?)', 'GCG > GCA', 'p.(=)', 'ACTA1_00194', 'known polymorphism', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.551G>A', '-', 'r.(?)', 'GGC > GAC', 'p.(Gly184Asp)', 'ACTA1_00065', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.553C>A', '-', 'r.(?)', 'CGC > AGC', 'p.(Arg185Ser)', 'ACTA1_00070', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.553C>G', '-', 'r.(?)', 'CGC > GGC', 'p.(Arg185Gly)', 'ACTA1_00068', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/11333380,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15198992', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.553C>T', '-', 'r.(?)', 'CGC > TGC', 'p.(Arg185Cys)', 'ACTA1_00067', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.554G>T', '-', 'r.(?)', 'CGC > CTC', 'p.(Arg185Leu)', 'ACTA1_00069', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.556G>C', '-', 'r.(?)', 'GAT > CAT', 'p.(Asp186His)', 'ACTA1_00220', '-', 'de novo', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.556G>T', '-', 'r.(?)', 'GAT > TAT', 'p.(Asp186Tyr)', 'ACTA1_00251', '-', 'de novo', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.557A>G', '-', 'r.(?)', 'GAT > GGT', 'p.(Asp186Gly)', 'ACTA1_00169', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.570C>A', '-', 'r.(?)', 'TAC > TAA', 'p.(Tyr190*)', 'ACTA1_00071', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.579G>T', '-', 'r.(?)', 'AAG > AAT', 'p.(Lys193Asn)', 'ACTA1_00072', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.586A>C', '-', 'r.(?)', 'ACT > CCT', 'p.(Thr196Pro)', 'ACTA1_00198', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.591G>T', '-', 'r.(?)', 'GAG > GAT', 'p.(Glu197Asp)', 'ACTA1_00241', '-', 'germline (inherited)', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['4', 'NM_001100.3:c.592C>A', '-', 'r.(?)', 'CGC > AGC', 'p.(Arg198Ser)', 'ACTA1_00188', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.592C>T', '-', 'r.(?)', 'CGT > TGT', 'p.(Arg198Cys)', 'ACTA1_00073', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.593G>A', '-', 'r.(?)', 'CGT > CAT', 'p.(Arg198His)', 'ACTA1_00075', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.593G>T', '-', 'r.(?)', 'CGT > CTT', 'p.(Arg198Leu)', 'ACTA1_00074', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.595G>A', '-', 'r.(?)', 'GGC > AGC', 'p.(Gly199Ser)', 'ACTA1_00076', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.598T>C', '-', 'r.(?)', 'TAC > CAC', 'p.(Tyr200His)', 'ACTA1_00232', '-', 'de novo', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.599A>G', '-', 'r.(?)', 'TAC > TGC', 'p.(Tyr200Cys)', 'ACTA1_00077', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_001100.3:c.616G>A', '-', 'r.(?)', 'GCT > ACT', 'p.(Ala206Thr)', 'ACTA1_00078', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4i', 'NM_001100.3:c.616+1G>A', '-', 'r.spl?', '-', '-', 'ACTA1_00140', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['4i', 'NM_001100.3:c.617-5C>A', '-', 'r.616_617ins617-3_617-1', '-', 'p.Thr205_Ala206insAla', 'ACTA1_00203', 'creation cryptic splice acceptor site predicted (+insert Ala translated from intron 4)', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['5', 'NM_001100.3:c.620A>G', '-', 'r.(?)', 'GAG > GGG', 'p.(Glu207Gly)', 'ACTA1_00170', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.621G>C', '-', 'r.(?)', 'GAG > GAC', 'p.(Glu207Asp)', 'ACTA1_00079', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.627G>C', '-', 'r.(?)', 'GAG > GAC', 'p.(Glu209Asp)', 'ACTA1_00080', 'pathogenicity unclear', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.649A>T', '-', 'r.(?)', 'AAG > TAG', 'p.(Lys217*)', 'ACTA1_00171', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.667C>G', '-', 'r.(?)', 'CTG > GTG', 'p.(Leu223Val)', 'ACTA1_00234', '-', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.668T>C', 'L221P', 'r.(?)', 'CTG > CCG', 'p.(Leu223Pro)', 'ACTA1_00081', 'not in >300 control chromosomes', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15468086,http://www.omim.org/entry/102610#0012', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.676G>C', '-', 'r.(?)', 'GAG > CAG', 'p.(Glu226Gln)', 'ACTA1_00082', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.677A>G', '-', 'r.(?)', 'GAG > GGG', 'p.(Glu226Gly)', 'ACTA1_00083', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.682G>C', '-', 'r.(?)', 'GAG > CAG', 'p.(Glu228Gln)', 'ACTA1_00172', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.685A>G', '-', 'r.(?)', 'ATG > GTG', 'p.(Met229Val)', 'ACTA1_00084', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.686T>C', '-', 'r.(?)', 'ATG > ACG', 'p.(Met229Thr)', 'ACTA1_00085', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.687G>A', '-', 'r.(?)', 'ATG > ATA', 'p.(Met229Ile)', 'ACTA1_00086', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.687G>C', '-', 'r.(?)', 'ATG > ATC', 'p.(Met229Ile)', 'ACTA1_00087', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.687G>T', '-', 'r.(?)', 'ATG > ATT', 'p.(Met229Ile)', 'ACTA1_00088', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.695C>T', '-', 'r.(?)', 'GCC > GTC', 'p.(Ala232Val)', 'ACTA1_00089', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.715G>A', '-', 'r.(?)', 'GAA>AAA', 'p.Glu239Lys', 'ACTA1_00223', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/21570694', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.715G>T', '-', 'r.(?)', 'GAA > TAA', 'p.(Glu239*)', 'ACTA1_00173', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.727G>A', '-', 'r.(?)', 'GAG > AAG', 'p.(Glu243Lys)', 'ACTA1_00090', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.737A>C', '-', 'r.(?)', 'GAC > GCC', 'p.(Asp246Ala)', 'ACTA1_00240', '-', 'germline (inherited)', '-', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.738C>A', '-', 'r.(?)', 'GAC > GAA', 'p.(Asp246Glu)', 'ACTA1_00174', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.739G>A', '-', 'r.(?)', 'GGG > AGG', 'p.(Gly247Arg)', 'ACTA1_00242', '-', 'germline (inherited)', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['5', 'NM_001100.3:c.739G>C', '-', 'r.(?)', 'GGG > CGG', 'p.(Gly247Arg)', 'ACTA1_00091', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.742C>A', '-', 'r.(?)', 'CAG > AAG', 'p.(Gln248Lys)', 'ACTA1_00092', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.743A>G', '-', 'r.(?)', 'CAG > CGG', 'p.(Gln248Arg)', 'ACTA1_00093', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.758G>A', '-', 'r.(?)', 'GGC > GAC', 'p.(Gly253Asp)', 'ACTA1_00094', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.760A>T', '-', 'r.(?)', 'AAC > TAC', 'p.(Asn254Tyr)', 'ACTA1_00175', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.764A>G', '-', 'r.(?)', 'GAG > GGG', 'p.(Glu255Gly)', 'ACTA1_00209', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.770T>G', '-', 'r.(?)', 'TTC > TGC', 'p.(Phe257Cys)', 'ACTA1_00183', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.773G>A', '-', 'r.(?)', 'CGC > CAC', 'p.(Arg258His)', 'ACTA1_00095', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.773G>T', '-', 'r.(?)', 'CGC > CTC', 'p.(Arg258Leu)', 'ACTA1_00096', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.782A>T', 'Glu259Val', 'r.(?)', 'GAG > GTG', 'p.(Glu261Val)', 'ACTA1_00097', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.omim.org/entry/102610#0005', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.794A>T', '-', 'r.(?)', 'CAG > CTG', 'p.(Gln265Leu)', 'ACTA1_00098', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/11748499,http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.796C>A', '-', 'r.(?)', 'CCC > ACC', 'p.(Pro266Thr)', 'ACTA1_00099', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.800C>G', '-', 'r.(?)', 'TCC > TGC', 'p.(Ser267Cys)', 'ACTA1_00177', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.802T>C', '-', 'r.(?)', 'TTC > CTC', 'p.(Phe268Leu)', 'ACTA1_00100', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.807_808delinsAA', '807_808delCGinsAA', 'r.(?)', 'GGT > AGT', 'p.(Gly270Ser)', 'ACTA1_00213', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.808G>A', '-', 'r.(?)', 'GGT > AGT', 'p.(Gly270Ser)', 'ACTA1_00101', 'consanguineous parents', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.808G>C', '-', 'r.(?)', 'GGT > CGT', 'p.(Gly270Arg)', 'ACTA1_00102', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_001100.3:c.808G>T', 'G268C', 'r.(?)', 'GGT > TGT', 'p.(Gly270Cys)', 'ACTA1_00103', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/11333380,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.omim.org/entry/102610#0007', 'DNA', 'SEQ', '-', '-'], ['5i', 'NM_001100.3:c.809-35delG', '-', 'r.(=)', '-', '-', 'ACTA1_00154', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['5i', 'NM_001100.3:c.809-15dup', '809-15dupC', 'r.(?)', '-', 'p.(=)', 'ACTA1_00237', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['5i', 'NM_001100.3:c.809-14G>C', '-', 'r.(=)', '-', '-', 'ACTA1_00155', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['5i', 'NM_001100.3:c.809-12dupC', '-', 'r.(=)', '-', '-', 'ACTA1_00214', 'known polymorphism', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['5i', 'NM_001100.3:c.809-2A>T', '-', 'r.spl?', '-', 'p.(?)', 'ACTA1_00201', '?recessive variant', 'germline (inherited)', '-', 'DNA', 'SEQ', '-', '-'], ['5i', 'NM_001100.3:c.809-1G>T', '-', 'r.spl?', '-', '-', 'ACTA1_00141', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.809G>A', '-', 'r.(?)', 'GGT > GAT', 'p.(Gly270Asp)', 'ACTA1_00104', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/15336687', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.812T>G', '-', 'r.(?)', 'ATG > AGG', 'p.(Met271Arg)', 'ACTA1_00105', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.814G>C', '-', 'r.(?)', 'GAG > CAG', 'p.(Glu272Gln)', 'ACTA1_00179', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.818C>G', '-', 'r.(?)', 'TCG > TGG', 'p.(Ser273Trp)', 'ACTA1_00249', '-', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.821C>A', '-', 'r.(?)', 'GCG > GAG', 'p.(Ala274Glu)', 'ACTA1_00106', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.824G>C', '-', 'r.(?)', '275', 'p.(Gly275Ala)', 'ACTA1_00244', '-', 'de novo', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['6', 'NM_001100.3:c.834G>T', '-', 'r.(?)', '-', 'p.(Glu278Asp)', 'ACTA1_00238', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.841T>C', '-', 'r.(?)', 'TAC > CAC', 'p.(Tyr281His)', 'ACTA1_00107', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.846C>G', '-', 'r.(?)', 'AAC > AAG', 'p.(Asn282Lys)', 'ACTA1_00108', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.854T>A', '-', 'r.(?)', 'ATG > AAG', 'p.(Met285Lys)', 'ACTA1_00109', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.854T>G', '-', 'r.(?)', 'ATG > AGG', 'p.(Met285Arg)', 'ACTA1_00110', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.863A>G', '-', 'r.(?)', 'GAC > GGC', 'p.(Asp288Gly)', 'ACTA1_00111', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.868G>A', '-', 'r.(?)', 'GAC > AAC', 'p.(Asp290Asn)', 'ACTA1_00180', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.871A>T', '-', 'r.(?)', 'ATC > TTC', 'p.(Ile291Phe)', 'ACTA1_00112', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.880G>T', '-', 'r.(?)', 'GAC > TAC', 'p.(Asp294Tyr)', 'ACTA1_00222', '-', 'germline (inherited)', '-', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.881A>T', 'D292V', 'r.(?)', 'GAC > GTC', 'p.(Asp294Val)', 'ACTA1_00113', 'not in >300 control chromosomes', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15468086,http://www.omim.org/entry/102610#0011', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.902T>A', '-', 'r.(?)', 'ATG > AAG', 'p.(Met301Lys)', 'ACTA1_00114', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.920T>G', '-', 'r.?', 'ATG > AGG', 'p.(Met307Arg)', 'ACTA1_00228', 'de novo, in patient', 'de novo', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['6', 'NM_001100.3:c.923A>G', '-', 'r.(?)', 'TAC > TGC', 'p.(Tyr308Cys)', 'ACTA1_00230', '-', 'unknown', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['6', 'NM_001100.3:c.925C>T', '-', 'r.(?)', 'CCT > TCT', 'p.(Pro309Ser)', 'ACTA1_00243', '-', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.980T>A', 'c.981T>A (p.M326K)', 'r.(?)', 'ATG > AAG', 'p.(Met327Lys)', 'ACTA1_00252', '-', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.983_985del', '982_984delAAG', 'r.(?)', '-', 'p.(Lys328del)', 'ACTA1_00205', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_001100.3:c.984G>C', '-', 'r.(?)', 'AAG > AAC', 'p.(Lys328Asn)', 'ACTA1_00199', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['6i', 'NM_001100.3:c.990+1G>T', '-', 'r.spl?', '-', '-', 'ACTA1_00142', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.996C>A', 'Ile332Ile', 'r.(?)', 'ATC > ATA', 'p.(=)', 'ACTA1_00147', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/10528865', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1000C>T', 'P332S', 'r.(?)', 'CCG > TGG', 'p.(Pro334Ser)', 'ACTA1_00117', 'not in >300 control chromosomes', 'unknown', 'http://www.ncbi.nlm.nih.gov/pubmed/15468086,http://www.omim.org/entry/102610#0013', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1001C>G', '-', 'r.(?)', 'CCG > CGG', 'p.(Pro334Arg)', 'ACTA1_00204', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1001C>T', '-', 'r.(?)', 'CCG > CTG', 'p.(Pro334Leu)', 'ACTA1_00247', '-', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1006G>A', '-', 'r.(?)', 'GAG > AAG', 'p.(Glu336Lys)', 'ACTA1_00211', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1006G>C', '-', 'r.(?)', 'GAG > CAG', 'p.(Glu336Gln)', 'ACTA1_00226', '-', 'germline (inherited)', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['7', 'NM_001100.3:c.1007A>C', 'E334A', 'r.(?)', 'GAG > GCG', 'p.(Glu336Ala)', 'ACTA1_00119', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15520409,http://www.omim.org/entry/102610#0010', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1012A>G', '-', 'r.(?)', 'AAA > GAA', 'p.(Lys338Glu)', 'ACTA1_00120', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/16945537', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1013A>T', '-', 'r.(?)', 'AAA > ATA', 'p.(Lys338Ile)', 'ACTA1_00121', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1019C>G', '-', 'r.(?)', 'TCG > TGG', 'p.(Ser340Trp)', 'ACTA1_00233', '-', 'unknown', '-', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1031delG', '-', 'r.(?)', '-', 'p.(Gly344Alafs*77)', 'ACTA1_00122', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/15236405', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1049C>T', '-', 'r.(?)', 'TCG > TTG', 'p.(Ser350Leu)', 'ACTA1_00123', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1057A>G', '-', 'r.(?)', 'ACC > GCC', 'p.(Thr353Ala)', 'ACTA1_00224', '-', 'de novo', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['7', 'NM_001100.3:c.1061T>A', '-', 'r.(?)', 'TTC > TAC', 'p.(Phe354Tyr)', 'ACTA1_00159', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1061T>C', '-', 'r.(?)', 'TTC > TCC', 'p.(Phe354Ser)', 'ACTA1_00124', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1074G>T', '-', 'r.(?)', 'TGG > TGT', 'p.(Trp358Cys)', 'ACTA1_00248', '-', 'unknown', 'http://www.ncbi.nlm.nih.gov/pubmed/23650303', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1075A>C', 'I357L', 'r.(?)', 'ATC > CTC', 'p.(Ile359Leu)', 'ACTA1_00125', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/11333380,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15198992,http://www.omim.org/entry/102610#0006', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1076T>C', '-', 'r.(?)', 'ATC > ACC', 'p.(Ile359Thr)', 'ACTA1_00250', '-', 'de novo', '-', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1092delC', '-', 'r.(?)', '-', 'p.(Tyr364*)', 'ACTA1_00126', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/17187373', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1106C>T', '-', 'r.(?)', 'CCT > CTT', 'p.(Pro369Leu)', 'ACTA1_00127', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1111A>C', '-', 'r.(?)', 'ATC > CTC', 'p.(Ile371Leu)', 'ACTA1_00128', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1114G>T', '-', 'r.(?)', 'GTC > TTC', 'p.(Val372Phe)', 'ACTA1_00129', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/10508519,http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1120C>A', '-', 'r.(?)', 'CGC > AGC', 'p.(Arg374Ser)', 'ACTA1_00130', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/12921789', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1120C>T', '-', 'r.(?)', 'CGC > TGC', 'p.(Arg374Cys)', 'ACTA1_00131', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1123A>C', '-', 'r.(?)', 'AAA > CAA', 'p.(Lys375Gln)', 'ACTA1_00132', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/11525890,http://www.ncbi.nlm.nih.gov/pubmed/12921789,http://www.ncbi.nlm.nih.gov/pubmed/15138616', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1123A>G', '-', 'r.(?)', 'AAA > GAA', 'p.(Lys375Glu)', 'ACTA1_00133', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/15336687', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1125A>C', '-', 'r.(?)', 'AAA > AAC', 'p.(Lys375Asn)', 'ACTA1_00181', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1127G>C', '-', 'r.(?)', 'TGC > TCC', 'p.(Cys376Ser)', 'ACTA1_00182', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1130T>A', '-', 'r.(?)', 'TTC > TAC', 'p.(Phe377Tyr)', 'ACTA1_00134', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/19562689', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1130T>G', '-', 'r.(?)', 'TTC > TGC', 'p.(Phe377Cys)', 'ACTA1_00135', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/16967490', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1132T>C', '-', 'r.(?)', 'TAG > CAG', 'p.(*378Glnext*47)', 'ACTA1_00136', '-', 'germline (inherited)', 'http://www.ncbi.nlm.nih.gov/pubmed/16945536', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1133A>G', '-', 'r.(?)', 'TAG > TGG', 'p.(*378Trpext*47)', 'ACTA1_00137', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/16945536', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_001100.3:c.1134G>T', '-', 'r.(?)', 'TAG > TAT', 'p.(*378Tyrext*47)', 'ACTA1_00138', '-', 'de novo', 'http://www.ncbi.nlm.nih.gov/pubmed/16945536', 'DNA', 'SEQ', '-', '-']]

CAPN3_GENE_HOMEPAGE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>CAPN3 homepage - Leiden Muscular Dystrophy pages - Leiden Open Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
  <META name="Author" content="LOVD development team, LUMC, Netherlands">
  <META name="Generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <LINK rel="stylesheet" type="text/css" href="./styles.css">
  <LINK rel="shortcut icon" href="./favicon.ico">
  <LINK rel="alternate" type="application/atom+xml" title="Leiden Muscular Dystrophy pages Atom 1.0 feed" href="./api/feed.php" />

  <SCRIPT type="text/javascript">
    <!--
    navHome_B     = new Image();
    navHome_B.src = './gfx/tab_home_B.png';
    navHome_H     = new Image();
    navHome_H.src = './gfx/tab_home_H.png';
    navVariants_B     = new Image();
    navVariants_B.src = './gfx/tab_variants_B.png';
    navVariants_H     = new Image();
    navVariants_H.src = './gfx/tab_variants_H.png';
    navSubmitters_B     = new Image();
    navSubmitters_B.src = './gfx/tab_submitters_B.png';
    navSubmitters_H     = new Image();
    navSubmitters_H.src = './gfx/tab_submitters_H.png';
    navSubmit_B     = new Image();
    navSubmit_B.src = './gfx/tab_submit_B.png';
    navSubmit_H     = new Image();
    navSubmit_H.src = './gfx/tab_submit_H.png';
    navDocs_B     = new Image();
    navDocs_B.src = './gfx/tab_docs_B.png';
    navDocs_H     = new Image();
    navDocs_H.src = './gfx/tab_docs_H.png';

    // Used for tab images.
    function lovd_imageSwitch (image_id, image_mode) {
      document.getElementById(image_id).src = eval(image_id + '_' + image_mode + '.src');
    }

    function lovd_switchGeneInline () {
      varForm = '<FORM action="/nmdb2/home.php" id="SelectGeneDBInline" method="get" style="margin : 0px;"><SELECT name="select_db" onchange="document.getElementById(\'SelectGeneDBInline\').submit();"><OPTION value="ACTA1">ACTA1 (ACTin, Alpha 1 (skeletal muscle))</OPTION><OPTION value="ACTC1">ACTC1 (Actin, alpha, cardiac muscle 1)</OPTION><OPTION value="AGRN">AGRN (Agrin)</OPTION><OPTION value="ANKRD1">ANKRD1 (Ankyrin repeat domain 1 (cardiac muscle))</OPTION><OPTION value="ANO5">ANO5 (Anoctamin 5)</OPTION><OPTION value="ARHGEF10">ARHGEF10 (Rho guanine nucleotide exchange factor (GEF) 10)</OPTION><OPTION value="ASAH1">ASAH1 (N-acylsphingosine amidohydrolase (acid ceramidase) 1)</OPTION><OPTION value="ATL1">ATL1 (Atlastin GTPase 1)</OPTION><OPTION value="B3GALNT2">B3GALNT2 (Beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION><OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION><OPTION value="BAG3">BAG3 (BCL2-associated athanogene 3)</OPTION><OPTION value="BANF1">BANF1 (Barrier to autointegration factor 1)</OPTION><OPTION value="BIN1">BIN1 (Bridging INtegrator 1)</OPTION><OPTION value="BSCL2">BSCL2 (Berardinelli-Seip congenital lipodystrophy 2 (seipin))</OPTION><OPTION value="CAPN3" selected>CAPN3 (Calpain-3)</OPTION><OPTION value="CAV3">CAV3 (Caveolin-3)</OPTION><OPTION value="CCDC78">CCDC78 (Coiled-coil domain containing 78)</OPTION><OPTION value="CCT5">CCT5 (Chaperonin containing TCP1, subunit 5 (epsilon))</OPTION><OPTION value="CFL2">CFL2 (Cofilin 2)</OPTION><OPTION value="CHAT">CHAT (Choline O-acetyltransferase)</OPTION><OPTION value="CHKB">CHKB (Choline kinase beta)</OPTION><OPTION value="CHRNA1">CHRNA1 (cholinergic receptor, nicotinic, alpha 1 (muscle))</OPTION><OPTION value="CHRNB1">CHRNB1 (Cholinergic receptor, nicotinic, beta 1 (muscle))</OPTION><OPTION value="CHRND">CHRND (Cholinergic receptor, nicotinic, delta)</OPTION><OPTION value="CHRNE">CHRNE (Cholinergic receptor, nicotinic, epsilon)</OPTION><OPTION value="CNTN1">CNTN1 (Contactin 1)</OPTION><OPTION value="COL6A1">COL6A1 (Collagen type VI alpha 1)</OPTION><OPTION value="COL6A2">COL6A2 (Collagen type VI alpha 2)</OPTION><OPTION value="COL6A3">COL6A3 (Collagen type VI alpha 3)</OPTION><OPTION value="COLQ">COLQ (Collagen-like tail subunit (single strand of homotrimer) of asymme...))</OPTION><OPTION value="CRYAB">CRYAB (Crystallin, alpha-B)</OPTION><OPTION value="CTDP1">CTDP1 (CTD (carboxy-terminal domain, RNA polymerase II, polypeptide A) p...))</OPTION><OPTION value="DAG1">DAG1 (Dystrophin-Associated Glycoprotein 1)</OPTION><OPTION value="DCTN1">DCTN1 (dynactin 1)</OPTION><OPTION value="DES">DES (Desmin)</OPTION><OPTION value="DMD">DMD (Duchenne Muscular Dystrophy)</OPTION><OPTION value="DMD_d">DMD_d (Duchenne Muscular Dystrophy (whole exon changes))</OPTION><OPTION value="DNAJB6">DNAJB6 (DnaJ (Hsp40) homolog, subfamily B, member 6)</OPTION><OPTION value="DNM2">DNM2 (Dynamin 2)</OPTION><OPTION value="DOK7">DOK7 (Docking protein 7)</OPTION><OPTION value="DPM3">DPM3 (Dolichyl-Phosphate Mannosyltransferase polypeptide 3)</OPTION><OPTION value="DTNA">DTNA (Dystrobrevin alpha)</OPTION><OPTION value="DUX4">DUX4 (Double homeobox 4)</OPTION><OPTION value="DYSF">DYSF (Dysferlin)</OPTION><OPTION value="EGR2">EGR2 (early growth response 2)</OPTION><OPTION value="EMD">EMD (Emery-Dreifuss muscular dystrophy (emerin))</OPTION><OPTION value="FAM134B">FAM134B (family with sequence similarity 134, member B)</OPTION><OPTION value="FGD4">FGD4 (FYVE, RhoGEF and PH domain containing 4)</OPTION><OPTION value="FHL1">FHL1 (Four and a Half LIM domains 1)</OPTION><OPTION value="FIG4">FIG4 (FIG4 homolog, SAC1 lipid phosphatase domain containing (S. cerevis...))</OPTION><OPTION value="FKRP">FKRP (Fukutin-Related Protein)</OPTION><OPTION value="FKTN">FKTN (Fukutin)</OPTION><OPTION value="FLNC">FLNC (Filamin C)</OPTION><OPTION value="GAN">GAN (Gigaxonin)</OPTION><OPTION value="GARS">GARS (glycyl-tRNA synthetase)</OPTION><OPTION value="GDAP1">GDAP1 (ganglioside induced differentiation associated protein 1)</OPTION><OPTION value="GFPT1">GFPT1 (Glutamine-fructose-6-phosphate transaminase 1)</OPTION><OPTION value="GJB1">GJB1 (gap junction protein, beta 1, 32kDa)</OPTION><OPTION value="GK">GK (Glycerol Kinase)</OPTION><OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION><OPTION value="GNB4">GNB4 (Guanine nucleotide binding protein (G protein), beta polypeptide 4)</OPTION><OPTION value="GNE">GNE (glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase)</OPTION><OPTION value="GTDC2">GTDC2 (Glycosyltransferase-like domain containing 2)</OPTION><OPTION value="HSPB1">HSPB1 (heat shock 27kDa protein 1)</OPTION><OPTION value="HSPB3">HSPB3 (heat shock 27kDa protein 3)</OPTION><OPTION value="HSPB8">HSPB8 (heat shock 22kDa protein 8)</OPTION><OPTION value="IGHMBP2">IGHMBP2 (Immunoglobulin mu binding protein 2)</OPTION><OPTION value="IKBKAP">IKBKAP (inhibitor of kappa light polypeptide gene enhancer in B-cells, k...)</OPTION><OPTION value="ISCU">ISCU (Iron-Sulfur cluster scaffold homolog (E. coli))</OPTION><OPTION value="ITGA7">ITGA7 (Integrin, alpha 7)</OPTION><OPTION value="KBTBD13">KBTBD13 (Kelch repeat and BTB (POZ) domain containing 13)</OPTION><OPTION value="KIF1B">KIF1B (kinesin family member 1B)</OPTION><OPTION value="KLHL40">KLHL40 (Kelch-like family member 40)</OPTION><OPTION value="LAMA2">LAMA2 (Laminin-alpha 2 (merosin))</OPTION><OPTION value="LAMP2">LAMP2 (Lysosomal-associated membrane protein 2)</OPTION><OPTION value="LARGE">LARGE (LARGE like-glycosyltransferase)</OPTION><OPTION value="LDB3">LDB3 (LIM domain binding 3 (ZASP))</OPTION><OPTION value="LITAF">LITAF (lipopolysaccharide-induced TNF factor)</OPTION><OPTION value="LMNA">LMNA (Lamin A/C)</OPTION><OPTION value="MATR3">MATR3 (Matrin 3)</OPTION><OPTION value="MFN2">MFN2 (Mitofusin 2)</OPTION><OPTION value="MICU1">MICU1 (Mitochondrial calcium uptake 1)</OPTION><OPTION value="MPZ">MPZ (Myelin protein zero)</OPTION><OPTION value="MSTN">MSTN (Myostatin)</OPTION><OPTION value="MTM1">MTM1 (Myotubularin 1)</OPTION><OPTION value="MTMR14">MTMR14 (Myotubularin related protein 14)</OPTION><OPTION value="MTMR2">MTMR2 (myotubularin related protein 2)</OPTION><OPTION value="MUSK">MUSK (muscle, skeletal, receptor tyrosine kinase)</OPTION><OPTION value="MYBPC3">MYBPC3 (Myosin binding protein C, cardiac)</OPTION><OPTION value="MYH7">MYH7 (myosin, heavy chain 7, cardiac muscle, beta)</OPTION><OPTION value="MYL2">MYL2 (Myosin, light chain 2, regulatory, cardiac, slow)</OPTION><OPTION value="MYL3">MYL3 (Myosin, light chain 3, alkali; ventricular, skeletal, slow)</OPTION><OPTION value="MYOT">MYOT (Myotilin (Titin immunoglobulin domain))</OPTION><OPTION value="MYOZ1">MYOZ1 (Myozenin 1)</OPTION><OPTION value="MYOZ2">MYOZ2 (Myozenin 2)</OPTION><OPTION value="MYOZ3">MYOZ3 (Myozenin 3)</OPTION><OPTION value="MYPN">MYPN (Myopalladin)</OPTION><OPTION value="NDRG1">NDRG1 (N-myc downstream regulated 1)</OPTION><OPTION value="NEB">NEB (Nebulin)</OPTION><OPTION value="NEFL">NEFL (Neurofilament, light polypeptide)</OPTION><OPTION value="NGF">NGF (nerve growth factor (beta polypeptide))</OPTION><OPTION value="NTRK1">NTRK1 (neurotrophic tyrosine kinase, receptor, type 1)</OPTION><OPTION value="PABPN1">PABPN1 (PolyA binding protein, nuclear 1)</OPTION><OPTION value="PDK3">PDK3 (Pyruvate dehydrogenase kinase, isozyme 3)</OPTION><OPTION value="PDLIM3">PDLIM3 (PDZ and LIM domain 3)</OPTION><OPTION value="PLEC">PLEC (Plectin)</OPTION><OPTION value="PLEKHG5">PLEKHG5 (pleckstrin homology domain containing, family G (with RhoGef do...))</OPTION><OPTION value="PMP22">PMP22 (Peripheral myelin protein 22)</OPTION><OPTION value="POMGNT1">POMGNT1 (Protein O-linked Mannose beta1,2-N-acetylGlucosaminylTransferase)</OPTION><OPTION value="POMT1">POMT1 (Protein O-Mannosyltransferase 1)</OPTION><OPTION value="POMT2">POMT2 (Protein O-Mannosyltransferase 2)</OPTION><OPTION value="PRPS1">PRPS1 (phosphoribosyl pyrophosphate synthetase 1)</OPTION><OPTION value="PRX">PRX (periaxin)</OPTION><OPTION value="PTRF">PTRF (Polymerase I and Transcript Release Factor (cavin-1))</OPTION><OPTION value="RAB7A">RAB7A (RAB7A, member RAS oncogene family)</OPTION><OPTION value="RAPSN">RAPSN (Receptor-associated protein of the synapse)</OPTION><OPTION value="RYR1">RYR1 (RYanodine Receptor 1 (skeletal))</OPTION><OPTION value="SBF2">SBF2 (SET binding factor 2)</OPTION><OPTION value="SEPN1">SEPN1 (Selenoprotein 1)</OPTION><OPTION value="SEPT9">SEPT9 (septin 9)</OPTION><OPTION value="SETX">SETX (senataxin)</OPTION><OPTION value="SGCA">SGCA (Sarcoglycan-alpha)</OPTION><OPTION value="SGCB">SGCB (Sarcoglycan-beta)</OPTION><OPTION value="SGCD">SGCD (Sarcoglycan-delta)</OPTION><OPTION value="SGCE">SGCE (Sarcoglycan-epsilon)</OPTION><OPTION value="SGCG">SGCG (Sarcoglycan-gamma)</OPTION><OPTION value="SGCZ">SGCZ (Sarcoglycan-zeta)</OPTION><OPTION value="SH3TC2">SH3TC2 (SH3 domain and tetratricopeptide repeats 2)</OPTION><OPTION value="SLC12A6">SLC12A6 (solute carrier family 12 (potassium/chloride transporters), mem...))</OPTION><OPTION value="SMCHD1">SMCHD1 (Structural maintenance of chromosomes flexible hinge domain cont...)</OPTION><OPTION value="SMN1">SMN1 (Survival Motor Neuron 1)</OPTION><OPTION value="SOX10">SOX10 (SRY (sex determining region Y)-box 10)</OPTION><OPTION value="SPTLC1">SPTLC1 (serine palmitoyltransferase, long chain base subunit 1)</OPTION><OPTION value="SPTLC2">SPTLC2 (serine palmitoyltransferase, long chain base subunit 2)</OPTION><OPTION value="SSPN">SSPN (Sarcospan)</OPTION><OPTION value="SYNE1">SYNE1 (Spectrin repeat containing, Nuclear Envelope 1)</OPTION><OPTION value="SYNE2">SYNE2 (Spectrin repeat containing, Nuclear Envelope 2)</OPTION><OPTION value="TCAP">TCAP (Titin-cap (telethonin))</OPTION><OPTION value="TNNI2">TNNI2 (Troponin I type 2)</OPTION><OPTION value="TNNI3">TNNI3 (Troponin I type 3 (cardiac))</OPTION><OPTION value="TNNT1">TNNT1 (Troponin T type 1)</OPTION><OPTION value="TNNT2">TNNT2 (Troponin T type 2 (cardiac))</OPTION><OPTION value="TNNT3">TNNT3 (Troponin T type 3)</OPTION><OPTION value="TNPO3">TNPO3 (Transportin 3)</OPTION><OPTION value="TPM1">TPM1 (tropomyosin 1 (alpha))</OPTION><OPTION value="TPM2">TPM2 (Tropomyosin 2)</OPTION><OPTION value="TPM3">TPM3 (Tropomyosin 3)</OPTION><OPTION value="TRAPPC11">TRAPPC11 (Trafficking protein particle complex 11)</OPTION><OPTION value="TRDN">TRDN (Triadin)</OPTION><OPTION value="TRIM32">TRIM32 (Tripartite motif-containing 32)</OPTION><OPTION value="TTN">TTN (Titin)</OPTION><OPTION value="TTR">TTR (Transthyretin)</OPTION><OPTION value="VCP">VCP (Valosin-containing protein)</OPTION><OPTION value="VMA21">VMA21 (VMA21 vacuolar H+-ATPase homolog (S. cerevisiae))</OPTION><OPTION value="WNK1">WNK1 (WNK lysine deficient protein kinase 1)</OPTION><OPTION value="YARS">YARS (tyrosyl-tRNA synthetase)</OPTION><OPTION value="ZMPSTE24">ZMPSTE24 (Zinc MetalloPeptidase (STE24 homolog, yeast))</OPTION></SELECT><INPUT type="submit" value="Switch"></FORM>';
      document.getElementById('gene_name').innerHTML=varForm;
    }

    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="./inc-js-openwindow.php"></SCRIPT>
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD width="150">
      <IMG src="./gfx/LOVD_logo130x50.jpg" alt="LOVD - Leiden Open Variation Database" width="130" height="50">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">Leiden Muscular Dystrophy pages</H2>
      <H5 id="gene_name">Calpain-3 (CAPN3)&nbsp;<A href="#" onclick="javascript:lovd_switchGeneInline(); return false;"><IMG src="./gfx/lovd_database_switch_inline.png" width="23" height="23" alt="Switch gene" title="Switch gene database" align="top" border="0"></A></H5>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.2.0 Build 35 [ <A href="./status.php">Current LOVD status</A> ]<BR>
      <A href="./submitters.php?action=register"><B>Register as submitter</B></A> | <A href="./account_login.php"><B>Log in</B></A><BR>
    </TD>
  </TR>
  <TR>
    <TD width="150">&nbsp;</TD>
    <TD valign="top" colspan="2" style="padding-bottom : 2px;"><B>Curators: <A href="mailto:LMDp-DBm@JohanDenDunnen.nl">Johan den Dunnen</A> and <A href="mailto:Jacques.Beckmann@chuv.ch">Jacqui Beckmann</A></B></TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('./gfx/tab_fill.png');">
      <IMG src="./gfx/tab_0F.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/home.php?select_db=CAPN3"><IMG src="./gfx/tab_home_F.png" alt="CAPN3 homepage" title="CAPN3 homepage" width="41" height="30" align="left" id="navHome" border="0"></A>
      <IMG src="./gfx/tab_FB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/variants.php?action=search_unique&amp;select_db=CAPN3"><IMG src="./gfx/tab_variants_B.png" alt="View unique variants" title="View unique variants" width="56" height="30" align="left" id="navVariants" border="0" onmouseover="lovd_imageSwitch('navVariants', 'H');" onmouseout="lovd_imageSwitch('navVariants', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submitters.php?action=public_list"><IMG src="./gfx/tab_submitters_B.png" alt="Public list of submitters" title="Public list of submitters" width="75" height="30" align="left" id="navSubmitters" border="0" onmouseover="lovd_imageSwitch('navSubmitters', 'H');" onmouseout="lovd_imageSwitch('navSubmitters', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submit.php"><IMG src="./gfx/tab_submit_B.png" alt="Submit new data" title="Submit new data" width="50" height="30" align="left" id="navSubmit" border="0" onmouseover="lovd_imageSwitch('navSubmit', 'H');" onmouseout="lovd_imageSwitch('navSubmit', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/docs/index.php"><IMG src="./gfx/tab_docs_B.png" alt="LOVD manual table of contents" title="LOVD manual table of contents" width="110" height="30" align="left" id="navDocs" border="0" onmouseover="lovd_imageSwitch('navDocs', 'H');" onmouseout="lovd_imageSwitch('navDocs', 'B');"></A>
      <IMG src="./gfx/tab_B0.png" alt="" width="33" height="30" align="left">
    </TD>
  </TR>
</TABLE>

<DIV style="padding : 5px; margin-bottom : 5px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="submenu">
  <TR>
    <TD>
      <TABLE border="0" cellpadding="0" cellspacing="0">
        <TR>
          <TD align="center" style="background : #C8DCFA;"><A href="/nmdb2/home.php">CAPN3&nbsp;homepage</A></TD>
          <TD style="padding : 0px;">&nbsp;</TD>
          <TD align="center"><A href="/nmdb2/home.php?action=switch_db">Switch&nbsp;gene</A></TD>
        </TR>
      </TABLE>
    </TD>
  </TR>
</TABLE>
</DIV>




<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD>








      <IMG src="./gfx/header_gene_homepage.png" alt="LOVD CAPN3 homepage" width="500" height="30"><BR>
      <BR>
      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">General information</TH></TR>
        <TR>
          <TH valign="top" width="275">Gene name</TH>
          <TD>Calpain-3</TD></TR>
        <TR>
          <TH valign="top" width="275">Gene symbol</TH>
          <TD><B>CAPN3</B></TD></TR>
        <TR>
          <TH valign="top" width="275">Chromosome Location</TH>
          <TD>15q15.1-q21.1</TD></TR>
        <TR>
          <TH valign="top" width="275">Database location</TH>
          <TD><a href='http://www.DMD.nl'>the Leiden Muscular Dystrophy pages</a></TD></TR>
        <TR>
          <TH valign="top" width="275">Curator</TH>
          <TD><A href="mailto:LMDp-DBm@JohanDenDunnen.nl">Johan den Dunnen</A> and <A href="mailto:Jacques.Beckmann@chuv.ch">Jacqui Beckmann</A></TD></TR>
        <TR>
          <TH valign="top" width="275">PubMed references</TH>
          <TD>View all (unique) <A href="pubmed_references.php">PubMed references</A> in the CAPN3 database</TD></TR>
        <TR>
          <TH valign="top" width="275">Date of creation</TH>
          <TD>January 10, 1997</TD></TR>
        <TR>
          <TH valign="top" width="275">Last update</TH>
          <TD>April 21, 2014</TD></TR>
        <TR>
          <TH valign="top" width="275">Version</TH>
          <TD><B>CAPN3 140421</B></TD></TR>
        <TR>
          <TH valign="top" width="275">Add sequence variant</TH>
          <TD><A href="submit.php">Submit a sequence variant</A></TD></TR>
        <TR>
          <TH valign="top" width="275">First&nbsp;time&nbsp;submitters</TH>
          <TD><A href="submitters.php?action=register">Register here</A></TD></TR>
        <TR>
          <TH valign="top" width="275">Reference sequence file</TH>
          <TD><A href="http://www.dmd.nl/nmdb2/refseq/CAPN3_codingDNA.html">coding DNA reference sequence</A> for describing sequence variants</B></TD></TR>
        <TR>
          <TH valign="top" width="275">Genomic refseq ID</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?db=nucleotide&amp;sendto=t&amp;extrafeatpresent=1&amp;list_uids=NG_008660.1" target="_blank">NG_008660.1</A></TD></TR>
        <TR>
          <TH valign="top" width="275">Transcript refseq ID</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?db=nucleotide&amp;sendto=t&amp;extrafeatpresent=1&amp;list_uids=NM_000070.2" target="_blank">NM_000070.2</A></TD></TR>
        <TR>
          <TH valign="top" width="275">Exon/intron information</TH>
          <TD><A href="refseq/CAPN3_table.html" target="_blank">Exon/intron information table</A></TD></TR>
        <TR>
          <TH valign="top" width="275"><I>Total&nbsp;number&nbsp;of&nbsp;unique&nbsp;DNA&nbsp;variants&nbsp;reported</I></TH>
          <TD><B>484</B></TD></TR>
        <TR>
          <TH valign="top" width="275"><I>Total number of individuals with variant(s)</I></TH>
          <TD><B>1740</B></TD></TR>
        <TR>
          <TH valign="top" width="275"><I>Total number of variants reported</I></TH>
          <TD><B>2833</B></TD></TR>
        <TR>
          <TH valign="top" width="275">Subscribe to updates of this gene</TH>
          <TD><A href="api/feed.php?select_db=CAPN3" target="_blank"><IMG src="gfx/feed_icon.png" border="0"></A></TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">Graphical displays and utilities</TH></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_statistics.php">Summary tables</A></TH>
          <TD>Summary of all sequence variants in the CAPN3 database, sorted by type of variant (with graphical displays and statistics)</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="#" onclick="lovd_openWindow('./scripts/readingFrameChecker.php', 'ScriptsReadingFrameChecker', 800, 500); return false;" class="data">Reading-frame checker</A></TH>
          <TD>The Reading-frame checker generates a prediction of the effect of whole-exon changes</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="http://genome.ucsc.edu/cgi-bin/hgTracks?clade=mammal&amp;org=Human&amp;db=hg19&amp;position=chr15:42651648-42704565&amp;hgt.customText=http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FCAPN3%3Fformat%3Dtext%2Fbed" target="_blank">UCSC Genome Browser</A></TH>
          <TD>Show variants in the UCSC Genome Browser (<A href="http://genome.ucsc.edu/cgi-bin/hgTracks?clade=mammal&amp;org=Human&amp;db=hg19&amp;position=chr15:42651648-42704565&amp;hgt.customText=http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FCAPN3%3Fformat%3Dtext%2Fbed%26visibility%3D4" target="_blank">compact view</A>)</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="http://www.ensembl.org/Homo_sapiens/Location/View?r=15:42651648-42704565;contigviewbottom=url:http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FCAPN3%3Fformat%3Dtext%2Fbed%26name%3D%2FCAPN3%20variants=labels" target="_blank">Ensembl Genome Browser</A></TH>
          <TD>Show variants in the Ensembl Genome Browser (<A href="http://www.ensembl.org/Homo_sapiens/Location/View?r=15:42651648-42704565;contigviewbottom=url:http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FCAPN3%3Fformat%3Dtext%2Fbed%26name%3D%2FCAPN3%20variants=normal" target="_blank">compact view</A>)</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="http://www.ncbi.nlm.nih.gov/nuccore/NC_000015.9?report=graph&amp;v=42651648:42704565&amp;theme=Expanded&amp;content=7&amp;url=http%3A%2F%2Fwww.dmd.nl%2Fnmdb2%2Fapi%2Frest.php%2Fvariants%2FCAPN3%3Fformat%3Dtext%2Fbed" target="_blank">NCBI Sequence Viewer</A></TH>
          <TD>Show distribution histogram of variants in the NCBI Sequence Viewer</TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">Sequence variant tables</TH></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants.php?select_db=CAPN3&amp;action=view_unique">Unique sequence variants</A></TH>
          <TD>Listing of all unique sequence variants in the CAPN3 database, without patient data</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants.php?select_db=CAPN3&amp;action=view_all">Complete&nbsp;sequence&nbsp;variant&nbsp;listing</A></TH>
          <TD>Listing of all sequence variants in the CAPN3 database</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants.php?select_db=CAPN3&amp;action=search_unique&amp;search_pathogenic_=-">Variants&nbsp;with&nbsp;no&nbsp;known&nbsp;pathogenicity</A></TH>
          <TD>Listing of all CAPN3 variants reported to have no noticeable phenotypic effect (note: excluding variants of unknown effect)</TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">Search the database</TH></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_search.php?show=type">By&nbsp;type&nbsp;of&nbsp;variant</A></TH>
          <TD>View all sequence variants of a certain type</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_search.php?show=quick">Simple search</A></TH>
          <TD>Query the database by selecting the most important variables (exon number, type of variant, disease phenotype)</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_search.php?show=full">Advanced&nbsp;search</A></TH>
          <TD>Query the database by selecting a combination of variables</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_overview_origin.php">Based on patient origin</A></TH>
          <TD>View all variants based on your patient origin search terms</TD></TR>
        <TR>
          <TH valign="top" width="275"><A href="variants_search.php?action=count_all">Search&nbsp;through&nbsp;hidden&nbsp;entries</A></TH>
          <TD>Find the number of variant entries in the database (including hidden entries) matching your search terms.</TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" colspan="2" class="S15">Links to other resources</TH></TR>
        <TR>
          <TH valign="top" width="275">Homepage</TH>
          <TD><A href="http://www.dmd.nl/capn3_home.html" target="_blank">http://www.dmd.nl/capn3_home.html</A></TD></TR>
        <TR>
          <TH valign="top" width="275">HGNC</TH>
          <TD><A href="http://www.genenames.org/data/hgnc_data.php?hgnc_id=1480" target="_blank">1480</A></TD></TR>
        <TR>
          <TH valign="top" width="275">Entrez Gene</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=gene&amp;cmd=Retrieve&amp;dopt=full_report&amp;list_uids=825" target="_blank">825</A></TD></TR>
        <TR>
          <TH valign="top" width="275">OMIM - Gene</TH>
          <TD><A href="http://www.omim.org/entry/114240" target="_blank">114240</A></TD></TR>
        <TR>
          <TH valign="top" width="275">OMIM - Disease</TH>
          <TD><A href="http://www.omim.org/entry/253600" target="_blank">limb-girdle muscular dystrophy, type 2A (LGMD-2A)</A></TD></TR>
        <TR>
          <TH valign="top" width="275">HGMD</TH>
          <TD><A href="http://www.hgmd.cf.ac.uk/ac/gene.php?gene=CAPN3" target="_blank">CAPN3</A></TD></TR>
        <TR>
          <TH valign="top" width="275">GeneCards</TH>
          <TD><A href="http://www.genecards.org/cgi-bin/carddisp.pl?gene=CAPN3" target="_blank">CAPN3</A></TD></TR>
        <TR>
          <TH valign="top" width="275">GeneTests</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/sites/GeneTests/lab/gene/CAPN3" target="_blank">CAPN3</A></TD></TR></TABLE>

      <HR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="gene">
        <TR>
          <TH valign="top" class="S15">Copyright &amp; disclaimer</TH></TR>
        <TR class="S11">
          <TD>The contents of this LOVD database are the intellectual property of the respective curator(s). Any unauthorised use, copying, storage or distribution of this material without written permission from the curator(s) will lead to copyright infringement with possible ensuing litigation. Copyright &copy; 2014. All Rights Reserved. For further details, refer to Directive 96/9/EC of the European Parliament and the Council of March 11 (1996) on the legal protection of databases.<BR><BR>We have used all reasonable efforts to ensure that the information displayed on these pages and contained in the databases is of high quality. We make no warranty, express or implied, as to its accuracy or that the information is fit for a particular purpose, and will not be held responsible for any consequences arising out of any inaccuracies or omissions. Individuals, organisations and companies which use this database do so on the understanding that no liability whatsoever either direct or indirect shall rest upon the curator(s) or any of their employees or agents for the effects of any product, process or method that may be produced or adopted by any part, notwithstanding that the formulation of such product, process or method may be based upon information here provided.</TD></TR></TABLE>

<BR>







    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/2.0/" target="_blank">LOVD v.2.0</A> Build 35<BR>
  Enabled modules: recaptcha, showmaxdbid, mutalyzer<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_update_newest_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>

<SCRIPT type="text/javascript">
  <!--
  objImg = document.getElementById('mapping_progress');

function lovd_HTTPRequest (sURL) {
    // Create HTTP request object.
    var objHTTP;
    try {
        // W3C standard.
        objHTTP = new XMLHttpRequest();
    } catch (e) {
        // Internet Explorer?
        try {
            objHTTP = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                objHTTP = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
                // Ok, last try!
                try {
                    objHTTP = window.createRequest();
                } catch (e) {
                    // Never mind.
                    objHTTP = false;
                }
            }
        }
    }

    if (objHTTP) {
        objHTTP.open("GET", sURL, false);
        objHTTP.send(null);
        return objHTTP;

    } else {
        return false;
    }
}



  function lovd_mapVariants () {
    // Request file that will do the actual work.
    objHTTP = lovd_HTTPRequest("http://www.dmd.nl/nmdb2/ajax-map_variants.php");

    if (!objHTTP || objHTTP.status != 200) {
        // Don't try again.
        objImg.src = "./gfx/lovd_mapping_99.png";
        objImg.title = "There was a problem with LOVD while mapping variants to the genome.";
    } else {
        aResponse = objHTTP.responseText.split("\t");
        // 2010-05-03; 2.0-26; Verify output, to prevent PHP errors from freaking out the browser (= every 50 microseconds a new request).
        // Took (and shortened) the "is_numeric()" implementation from http://phpjs.org/functions/is_numeric:449 (thanks guys).
        if (aResponse.length == 2 && !isNaN(aResponse[0])) {
            objImg.src = "./gfx/lovd_mapping_" + aResponse[0] + ".png";
            objImg.title = aResponse[1];

            if (aResponse[1] != "All done!") {
                setTimeout("lovd_mapVariants()", 50);
            } else {
                objImg.setAttribute("onclick", "lovd_mapVariants();");
            }
        } else {
            objImg.title = "Error occured: " + objHTTP.responseText;
        }
    }
  }

objImg.setAttribute("onclick", "lovd_mapVariants();");
  // -->
</SCRIPT>

</BODY>
</HTML>
"""

CAPN3_VARIANT_DATABASE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>Search unique variants - Leiden Muscular Dystrophy pages - Leiden Open Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
  <META name="Author" content="LOVD development team, LUMC, Netherlands">
  <META name="Generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <LINK rel="stylesheet" type="text/css" href="./styles.css">
  <LINK rel="shortcut icon" href="./favicon.ico">
  <LINK rel="alternate" type="application/atom+xml" title="Leiden Muscular Dystrophy pages Atom 1.0 feed" href="./api/feed.php" />

  <SCRIPT type="text/javascript">
    <!--
    navHome_B     = new Image();
    navHome_B.src = './gfx/tab_home_B.png';
    navHome_H     = new Image();
    navHome_H.src = './gfx/tab_home_H.png';
    navVariants_B     = new Image();
    navVariants_B.src = './gfx/tab_variants_B.png';
    navVariants_H     = new Image();
    navVariants_H.src = './gfx/tab_variants_H.png';
    navSubmitters_B     = new Image();
    navSubmitters_B.src = './gfx/tab_submitters_B.png';
    navSubmitters_H     = new Image();
    navSubmitters_H.src = './gfx/tab_submitters_H.png';
    navSubmit_B     = new Image();
    navSubmit_B.src = './gfx/tab_submit_B.png';
    navSubmit_H     = new Image();
    navSubmit_H.src = './gfx/tab_submit_H.png';
    navDocs_B     = new Image();
    navDocs_B.src = './gfx/tab_docs_B.png';
    navDocs_H     = new Image();
    navDocs_H.src = './gfx/tab_docs_H.png';

    // Used for tab images.
    function lovd_imageSwitch (image_id, image_mode) {
      document.getElementById(image_id).src = eval(image_id + '_' + image_mode + '.src');
    }

    function lovd_switchGeneInline () {
      varForm = '<FORM action="/nmdb2/variants.php" id="SelectGeneDBInline" method="get" style="margin : 0px;"><SELECT name="select_db" onchange="document.getElementById(\'SelectGeneDBInline\').submit();"><OPTION value="ACTA1">ACTA1 (ACTin, Alpha 1 (skeletal muscle))</OPTION><OPTION value="ACTC1">ACTC1 (Actin, alpha, cardiac muscle 1)</OPTION><OPTION value="AGRN">AGRN (Agrin)</OPTION><OPTION value="ANKRD1">ANKRD1 (Ankyrin repeat domain 1 (cardiac muscle))</OPTION><OPTION value="ANO5">ANO5 (Anoctamin 5)</OPTION><OPTION value="ARHGEF10">ARHGEF10 (Rho guanine nucleotide exchange factor (GEF) 10)</OPTION><OPTION value="ASAH1">ASAH1 (N-acylsphingosine amidohydrolase (acid ceramidase) 1)</OPTION><OPTION value="ATL1">ATL1 (Atlastin GTPase 1)</OPTION><OPTION value="B3GALNT2">B3GALNT2 (Beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION><OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION><OPTION value="BAG3">BAG3 (BCL2-associated athanogene 3)</OPTION><OPTION value="BANF1">BANF1 (Barrier to autointegration factor 1)</OPTION><OPTION value="BIN1">BIN1 (Bridging INtegrator 1)</OPTION><OPTION value="BSCL2">BSCL2 (Berardinelli-Seip congenital lipodystrophy 2 (seipin))</OPTION><OPTION value="CAPN3" selected>CAPN3 (Calpain-3)</OPTION><OPTION value="CAV3">CAV3 (Caveolin-3)</OPTION><OPTION value="CCDC78">CCDC78 (Coiled-coil domain containing 78)</OPTION><OPTION value="CCT5">CCT5 (Chaperonin containing TCP1, subunit 5 (epsilon))</OPTION><OPTION value="CFL2">CFL2 (Cofilin 2)</OPTION><OPTION value="CHAT">CHAT (Choline O-acetyltransferase)</OPTION><OPTION value="CHKB">CHKB (Choline kinase beta)</OPTION><OPTION value="CHRNA1">CHRNA1 (cholinergic receptor, nicotinic, alpha 1 (muscle))</OPTION><OPTION value="CHRNB1">CHRNB1 (Cholinergic receptor, nicotinic, beta 1 (muscle))</OPTION><OPTION value="CHRND">CHRND (Cholinergic receptor, nicotinic, delta)</OPTION><OPTION value="CHRNE">CHRNE (Cholinergic receptor, nicotinic, epsilon)</OPTION><OPTION value="CNTN1">CNTN1 (Contactin 1)</OPTION><OPTION value="COL6A1">COL6A1 (Collagen type VI alpha 1)</OPTION><OPTION value="COL6A2">COL6A2 (Collagen type VI alpha 2)</OPTION><OPTION value="COL6A3">COL6A3 (Collagen type VI alpha 3)</OPTION><OPTION value="COLQ">COLQ (Collagen-like tail subunit (single strand of homotrimer) of asymme...))</OPTION><OPTION value="CRYAB">CRYAB (Crystallin, alpha-B)</OPTION><OPTION value="CTDP1">CTDP1 (CTD (carboxy-terminal domain, RNA polymerase II, polypeptide A) p...))</OPTION><OPTION value="DAG1">DAG1 (Dystrophin-Associated Glycoprotein 1)</OPTION><OPTION value="DCTN1">DCTN1 (dynactin 1)</OPTION><OPTION value="DES">DES (Desmin)</OPTION><OPTION value="DMD">DMD (Duchenne Muscular Dystrophy)</OPTION><OPTION value="DMD_d">DMD_d (Duchenne Muscular Dystrophy (whole exon changes))</OPTION><OPTION value="DNAJB6">DNAJB6 (DnaJ (Hsp40) homolog, subfamily B, member 6)</OPTION><OPTION value="DNM2">DNM2 (Dynamin 2)</OPTION><OPTION value="DOK7">DOK7 (Docking protein 7)</OPTION><OPTION value="DPM3">DPM3 (Dolichyl-Phosphate Mannosyltransferase polypeptide 3)</OPTION><OPTION value="DTNA">DTNA (Dystrobrevin alpha)</OPTION><OPTION value="DUX4">DUX4 (Double homeobox 4)</OPTION><OPTION value="DYSF">DYSF (Dysferlin)</OPTION><OPTION value="EGR2">EGR2 (early growth response 2)</OPTION><OPTION value="EMD">EMD (Emery-Dreifuss muscular dystrophy (emerin))</OPTION><OPTION value="FAM134B">FAM134B (family with sequence similarity 134, member B)</OPTION><OPTION value="FGD4">FGD4 (FYVE, RhoGEF and PH domain containing 4)</OPTION><OPTION value="FHL1">FHL1 (Four and a Half LIM domains 1)</OPTION><OPTION value="FIG4">FIG4 (FIG4 homolog, SAC1 lipid phosphatase domain containing (S. cerevis...))</OPTION><OPTION value="FKRP">FKRP (Fukutin-Related Protein)</OPTION><OPTION value="FKTN">FKTN (Fukutin)</OPTION><OPTION value="FLNC">FLNC (Filamin C)</OPTION><OPTION value="GAN">GAN (Gigaxonin)</OPTION><OPTION value="GARS">GARS (glycyl-tRNA synthetase)</OPTION><OPTION value="GDAP1">GDAP1 (ganglioside induced differentiation associated protein 1)</OPTION><OPTION value="GFPT1">GFPT1 (Glutamine-fructose-6-phosphate transaminase 1)</OPTION><OPTION value="GJB1">GJB1 (gap junction protein, beta 1, 32kDa)</OPTION><OPTION value="GK">GK (Glycerol Kinase)</OPTION><OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION><OPTION value="GNB4">GNB4 (Guanine nucleotide binding protein (G protein), beta polypeptide 4)</OPTION><OPTION value="GNE">GNE (glucosamine (UDP-N-acetyl)-2-epimerase/N-acetylmannosamine kinase)</OPTION><OPTION value="GTDC2">GTDC2 (Glycosyltransferase-like domain containing 2)</OPTION><OPTION value="HSPB1">HSPB1 (heat shock 27kDa protein 1)</OPTION><OPTION value="HSPB3">HSPB3 (heat shock 27kDa protein 3)</OPTION><OPTION value="HSPB8">HSPB8 (heat shock 22kDa protein 8)</OPTION><OPTION value="IGHMBP2">IGHMBP2 (Immunoglobulin mu binding protein 2)</OPTION><OPTION value="IKBKAP">IKBKAP (inhibitor of kappa light polypeptide gene enhancer in B-cells, k...)</OPTION><OPTION value="ISCU">ISCU (Iron-Sulfur cluster scaffold homolog (E. coli))</OPTION><OPTION value="ITGA7">ITGA7 (Integrin, alpha 7)</OPTION><OPTION value="KBTBD13">KBTBD13 (Kelch repeat and BTB (POZ) domain containing 13)</OPTION><OPTION value="KIF1B">KIF1B (kinesin family member 1B)</OPTION><OPTION value="KLHL40">KLHL40 (Kelch-like family member 40)</OPTION><OPTION value="LAMA2">LAMA2 (Laminin-alpha 2 (merosin))</OPTION><OPTION value="LAMP2">LAMP2 (Lysosomal-associated membrane protein 2)</OPTION><OPTION value="LARGE">LARGE (LARGE like-glycosyltransferase)</OPTION><OPTION value="LDB3">LDB3 (LIM domain binding 3 (ZASP))</OPTION><OPTION value="LITAF">LITAF (lipopolysaccharide-induced TNF factor)</OPTION><OPTION value="LMNA">LMNA (Lamin A/C)</OPTION><OPTION value="MATR3">MATR3 (Matrin 3)</OPTION><OPTION value="MFN2">MFN2 (Mitofusin 2)</OPTION><OPTION value="MICU1">MICU1 (Mitochondrial calcium uptake 1)</OPTION><OPTION value="MPZ">MPZ (Myelin protein zero)</OPTION><OPTION value="MSTN">MSTN (Myostatin)</OPTION><OPTION value="MTM1">MTM1 (Myotubularin 1)</OPTION><OPTION value="MTMR14">MTMR14 (Myotubularin related protein 14)</OPTION><OPTION value="MTMR2">MTMR2 (myotubularin related protein 2)</OPTION><OPTION value="MUSK">MUSK (muscle, skeletal, receptor tyrosine kinase)</OPTION><OPTION value="MYBPC3">MYBPC3 (Myosin binding protein C, cardiac)</OPTION><OPTION value="MYH7">MYH7 (myosin, heavy chain 7, cardiac muscle, beta)</OPTION><OPTION value="MYL2">MYL2 (Myosin, light chain 2, regulatory, cardiac, slow)</OPTION><OPTION value="MYL3">MYL3 (Myosin, light chain 3, alkali; ventricular, skeletal, slow)</OPTION><OPTION value="MYOT">MYOT (Myotilin (Titin immunoglobulin domain))</OPTION><OPTION value="MYOZ1">MYOZ1 (Myozenin 1)</OPTION><OPTION value="MYOZ2">MYOZ2 (Myozenin 2)</OPTION><OPTION value="MYOZ3">MYOZ3 (Myozenin 3)</OPTION><OPTION value="MYPN">MYPN (Myopalladin)</OPTION><OPTION value="NDRG1">NDRG1 (N-myc downstream regulated 1)</OPTION><OPTION value="NEB">NEB (Nebulin)</OPTION><OPTION value="NEFL">NEFL (Neurofilament, light polypeptide)</OPTION><OPTION value="NGF">NGF (nerve growth factor (beta polypeptide))</OPTION><OPTION value="NTRK1">NTRK1 (neurotrophic tyrosine kinase, receptor, type 1)</OPTION><OPTION value="PABPN1">PABPN1 (PolyA binding protein, nuclear 1)</OPTION><OPTION value="PDK3">PDK3 (Pyruvate dehydrogenase kinase, isozyme 3)</OPTION><OPTION value="PDLIM3">PDLIM3 (PDZ and LIM domain 3)</OPTION><OPTION value="PLEC">PLEC (Plectin)</OPTION><OPTION value="PLEKHG5">PLEKHG5 (pleckstrin homology domain containing, family G (with RhoGef do...))</OPTION><OPTION value="PMP22">PMP22 (Peripheral myelin protein 22)</OPTION><OPTION value="POMGNT1">POMGNT1 (Protein O-linked Mannose beta1,2-N-acetylGlucosaminylTransferase)</OPTION><OPTION value="POMT1">POMT1 (Protein O-Mannosyltransferase 1)</OPTION><OPTION value="POMT2">POMT2 (Protein O-Mannosyltransferase 2)</OPTION><OPTION value="PRPS1">PRPS1 (phosphoribosyl pyrophosphate synthetase 1)</OPTION><OPTION value="PRX">PRX (periaxin)</OPTION><OPTION value="PTRF">PTRF (Polymerase I and Transcript Release Factor (cavin-1))</OPTION><OPTION value="RAB7A">RAB7A (RAB7A, member RAS oncogene family)</OPTION><OPTION value="RAPSN">RAPSN (Receptor-associated protein of the synapse)</OPTION><OPTION value="RYR1">RYR1 (RYanodine Receptor 1 (skeletal))</OPTION><OPTION value="SBF2">SBF2 (SET binding factor 2)</OPTION><OPTION value="SEPN1">SEPN1 (Selenoprotein 1)</OPTION><OPTION value="SEPT9">SEPT9 (septin 9)</OPTION><OPTION value="SETX">SETX (senataxin)</OPTION><OPTION value="SGCA">SGCA (Sarcoglycan-alpha)</OPTION><OPTION value="SGCB">SGCB (Sarcoglycan-beta)</OPTION><OPTION value="SGCD">SGCD (Sarcoglycan-delta)</OPTION><OPTION value="SGCE">SGCE (Sarcoglycan-epsilon)</OPTION><OPTION value="SGCG">SGCG (Sarcoglycan-gamma)</OPTION><OPTION value="SGCZ">SGCZ (Sarcoglycan-zeta)</OPTION><OPTION value="SH3TC2">SH3TC2 (SH3 domain and tetratricopeptide repeats 2)</OPTION><OPTION value="SLC12A6">SLC12A6 (solute carrier family 12 (potassium/chloride transporters), mem...))</OPTION><OPTION value="SMCHD1">SMCHD1 (Structural maintenance of chromosomes flexible hinge domain cont...)</OPTION><OPTION value="SMN1">SMN1 (Survival Motor Neuron 1)</OPTION><OPTION value="SOX10">SOX10 (SRY (sex determining region Y)-box 10)</OPTION><OPTION value="SPTLC1">SPTLC1 (serine palmitoyltransferase, long chain base subunit 1)</OPTION><OPTION value="SPTLC2">SPTLC2 (serine palmitoyltransferase, long chain base subunit 2)</OPTION><OPTION value="SSPN">SSPN (Sarcospan)</OPTION><OPTION value="SYNE1">SYNE1 (Spectrin repeat containing, Nuclear Envelope 1)</OPTION><OPTION value="SYNE2">SYNE2 (Spectrin repeat containing, Nuclear Envelope 2)</OPTION><OPTION value="TCAP">TCAP (Titin-cap (telethonin))</OPTION><OPTION value="TNNI2">TNNI2 (Troponin I type 2)</OPTION><OPTION value="TNNI3">TNNI3 (Troponin I type 3 (cardiac))</OPTION><OPTION value="TNNT1">TNNT1 (Troponin T type 1)</OPTION><OPTION value="TNNT2">TNNT2 (Troponin T type 2 (cardiac))</OPTION><OPTION value="TNNT3">TNNT3 (Troponin T type 3)</OPTION><OPTION value="TNPO3">TNPO3 (Transportin 3)</OPTION><OPTION value="TPM1">TPM1 (tropomyosin 1 (alpha))</OPTION><OPTION value="TPM2">TPM2 (Tropomyosin 2)</OPTION><OPTION value="TPM3">TPM3 (Tropomyosin 3)</OPTION><OPTION value="TRAPPC11">TRAPPC11 (Trafficking protein particle complex 11)</OPTION><OPTION value="TRDN">TRDN (Triadin)</OPTION><OPTION value="TRIM32">TRIM32 (Tripartite motif-containing 32)</OPTION><OPTION value="TTN">TTN (Titin)</OPTION><OPTION value="TTR">TTR (Transthyretin)</OPTION><OPTION value="VCP">VCP (Valosin-containing protein)</OPTION><OPTION value="VMA21">VMA21 (VMA21 vacuolar H+-ATPase homolog (S. cerevisiae))</OPTION><OPTION value="WNK1">WNK1 (WNK lysine deficient protein kinase 1)</OPTION><OPTION value="YARS">YARS (tyrosyl-tRNA synthetase)</OPTION><OPTION value="ZMPSTE24">ZMPSTE24 (Zinc MetalloPeptidase (STE24 homolog, yeast))</OPTION></SELECT><INPUT type="hidden" name="action" value="search_unique"><INPUT type="submit" value="Switch"></FORM>';
      document.getElementById('gene_name').innerHTML=varForm;
    }

    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="./inc-js-openwindow.php"></SCRIPT>
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD width="150">
      <IMG src="./gfx/LOVD_logo130x50.jpg" alt="LOVD - Leiden Open Variation Database" width="130" height="50">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">Leiden Muscular Dystrophy pages</H2>
      <H5 id="gene_name">Calpain-3 (CAPN3)&nbsp;<A href="#" onclick="javascript:lovd_switchGeneInline(); return false;"><IMG src="./gfx/lovd_database_switch_inline.png" width="23" height="23" alt="Switch gene" title="Switch gene database" align="top" border="0"></A></H5>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.2.0 Build 35 [ <A href="./status.php">Current LOVD status</A> ]<BR>
      <A href="./submitters.php?action=register"><B>Register as submitter</B></A> | <A href="./account_login.php"><B>Log in</B></A><BR>
    </TD>
  </TR>
  <TR>
    <TD width="150">&nbsp;</TD>
    <TD valign="top" colspan="2" style="padding-bottom : 2px;"><B>Curators: <A href="mailto:LMDp-DBm@JohanDenDunnen.nl">Johan den Dunnen</A> and <A href="mailto:Jacques.Beckmann@chuv.ch">Jacqui Beckmann</A></B></TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('./gfx/tab_fill.png');">
      <IMG src="./gfx/tab_0B.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/home.php?select_db=CAPN3"><IMG src="./gfx/tab_home_B.png" alt="CAPN3 homepage" title="CAPN3 homepage" width="41" height="30" align="left" id="navHome" border="0" onmouseover="lovd_imageSwitch('navHome', 'H');" onmouseout="lovd_imageSwitch('navHome', 'B');"></A>
      <IMG src="./gfx/tab_BF.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/variants.php?action=search_unique&amp;select_db=CAPN3"><IMG src="./gfx/tab_variants_F.png" alt="View unique variants" title="View unique variants" width="56" height="30" align="left" id="navVariants" border="0"></A>
      <IMG src="./gfx/tab_FB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submitters.php?action=public_list"><IMG src="./gfx/tab_submitters_B.png" alt="Public list of submitters" title="Public list of submitters" width="75" height="30" align="left" id="navSubmitters" border="0" onmouseover="lovd_imageSwitch('navSubmitters', 'H');" onmouseout="lovd_imageSwitch('navSubmitters', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/submit.php"><IMG src="./gfx/tab_submit_B.png" alt="Submit new data" title="Submit new data" width="50" height="30" align="left" id="navSubmit" border="0" onmouseover="lovd_imageSwitch('navSubmit', 'H');" onmouseout="lovd_imageSwitch('navSubmit', 'B');"></A>
      <IMG src="./gfx/tab_BB.png" alt="" width="33" height="30" align="left">
      <A href="/nmdb2/docs/index.php"><IMG src="./gfx/tab_docs_B.png" alt="LOVD manual table of contents" title="LOVD manual table of contents" width="110" height="30" align="left" id="navDocs" border="0" onmouseover="lovd_imageSwitch('navDocs', 'H');" onmouseout="lovd_imageSwitch('navDocs', 'B');"></A>
      <IMG src="./gfx/tab_B0.png" alt="" width="33" height="30" align="left">
    </TD>
  </TR>
</TABLE>

<DIV style="padding : 5px; margin-bottom : 5px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="submenu">
  <TR>
    <TD>
      <TABLE border="0" cellpadding="0" cellspacing="0">
        <TR>
          <TD align="center"><A href="/nmdb2/variants.php?action=view_unique">View&nbsp;unique&nbsp;variants</A></TD>
          <TD style="padding : 0px;">&nbsp;</TD>
          <TD align="center" style="background : #C8DCFA;"><A href="/nmdb2/variants.php?action=search_unique">Search&nbsp;unique&nbsp;variants</A></TD>
          <TD width="1" style="padding : 0px; background : #224488;"><IMG src="./gfx/trans.png" alt="" width="1" height="1"></TD>
          <TD align="center"><A href="/nmdb2/variants.php?action=view_all">View&nbsp;all&nbsp;contents</A></TD>
          <TD style="padding : 0px;">&nbsp;</TD>
          <TD align="center"><A href="/nmdb2/variants.php?action=search_all">Full&nbsp;database&nbsp;search</A></TD>
          <TD width="1" style="padding : 0px; background : #224488;"><IMG src="./gfx/trans.png" alt="" width="1" height="1"></TD>
          <TD align="center"><A href="/nmdb2/variants_overview_origin.php">Variant&nbsp;listing&nbsp;based&nbsp;on&nbsp;patient&nbsp;origin</A></TD>
          <TD width="1" style="padding : 0px; background : #224488;"><IMG src="./gfx/trans.png" alt="" width="1" height="1"></TD>
          <TD align="center"><A href="/nmdb2/variants_statistics.php">Database&nbsp;statistics</A></TD>
          <TD style="padding : 0px;">&nbsp;</TD>
          <TD align="center"><A href="/nmdb2/home.php?action=switch_db">Switch&nbsp;gene</A></TD>
        </TR>
      </TABLE>
    </TD>
  </TR>
</TABLE>
</DIV>




<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD>








      <IMG src="./gfx/header_variant_listings.png" alt="LOVD - Variant listings for CAPN3" width="500" height="30"><BR>
      <BR>
      <FORM action="/nmdb2/variants.php" method="get" style="margin : 0px;">
        <INPUT type="hidden" name="select_db" value="CAPN3">
        <INPUT type="hidden" name="action" value="search_unique">
        <INPUT type="hidden" name="order" value="Variant/DNA,ASC">
        <INPUT type="hidden" name="hide_col" value="">
        <INPUT type="hidden" name="show_col" value="">

      <SCRIPT type="text/javascript" src="./inc-js-toggle-visibility.js"></SCRIPT>
      <TABLE border="0" cellpadding="0" cellspacing="0" width="960">
        <TR>
          <TD valign="top">
            <TABLE border="0" cellpadding="0" cellspacing="0" class="navigation">
              <TR align="center">
                <TD><A style="color : #999999;">Unhide all columns</A> | <A href="#" onclick="lovd_openWindow('views_columns.php?action=search_unique&amp;hide=true', 'HideColumns', 300, 500); return false;">Hide Specific Columns</A> | <A href="#" onclick="document.forms[0].hide_col.value='all';document.forms[0].submit();">Hide all columns</A></TD></TR></TABLE>

          </TD>
          <TD align="right">
            <TABLE border="0" cellpadding="2" cellspacing="0" width="525" class="info" style="font-size : 11px;">
              <TR>
                <TH>About this overview [<A href="#" id="moreinfo_link" onClick="lovd_toggleVisibility('moreinfo'); return false;">Show</A>]</TH>
              <TR id="moreinfo" style="display : none;">
                <TD>The variants below are all in the CAPN3 database, matching your query. In this view only variant fields are shown. Variants are listed only once, a number is present in the DNA change field when a variant has been reported more than once (in such cases fields other than the DNA change just belong to one entry and may differ for other entries).<BR>Selecting and clicking a specific line will open a detailed view showing all variant entries, including patient and pathogenicity information.<BR>At the bottom of this page a legend is provided with a short explanation of what each field contains.<BR>For a more detailed description of each field, please see the <A href="variants_legend.php?select_db=CAPN3" target="_blank">CAPN3 full legend</A> here.<BR></TD></TR></TABLE></TD></TR></TABLE><BR>

      <SPAN class="S11">485 entries</SPAN><BR>
      <SPAN class="S11"><SELECT name="limit" class="S11" onchange="document.forms[0].submit();">
        <OPTION value="25">25</OPTION>
        <OPTION value="50">50</OPTION>
        <OPTION value="100" selected>100</OPTION>
        <OPTION value="250">250</OPTION>
        <OPTION value="500">500</OPTION>
        <OPTION value="1000">1000</OPTION></SELECT> entries per page</SPAN><BR>

     <DIV id="table_div" style="height : 20px;">
      <TABLE border="0" cellpadding="0" cellspacing="1" class="data" id="table_headers" style="position : absolute; background : #FFFFFF;">
        <TR>
          <TH valign="top" width="50" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Exon,ASC';document.forms[0].submit();">
                <TH>Exon</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Exon column" title="Hide Exon column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Exon';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Exon" value="" title="Exon field should contain..." style="width : 42px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="ordered"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/DNA,DESC';document.forms[0].submit();">
                <TH>DNA&nbsp;change</TH>
                <TD align="right" width="13">&nbsp;</TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc_sel.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/DNA" value="" title="DNA change field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/DNA_published,ASC';document.forms[0].submit();">
                <TH>Var_pub_as</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Var_pub_as column" title="Hide Var_pub_as column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/DNA_published';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/DNA_published" value="" title="Var_pub_as field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/RNA,ASC';document.forms[0].submit();">
                <TH>RNA&nbsp;change</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide RNA change column" title="Hide RNA change column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/RNA';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/RNA" value="" title="RNA change field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Protein,ASC';document.forms[0].submit();">
                <TH>Protein&nbsp;change</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Protein change column" title="Hide Protein change column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Protein';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Protein" value="" title="Protein change field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="80" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/DBID,ASC';document.forms[0].submit();">
                <TH>DB-ID</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide DB-ID column" title="Hide DB-ID column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/DBID';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/DBID" value="" title="DB-ID field should contain..." style="width : 72px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Remarks,ASC';document.forms[0].submit();">
                <TH>Variant&nbsp;remarks</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Variant remarks column" title="Hide Variant remarks column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Remarks';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Remarks" value="" title="Variant remarks field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="100" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Genetic_origin,ASC';document.forms[0].submit();">
                <TH>Genet_ori</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Genet_ori column" title="Hide Genet_ori column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Genetic_origin';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Genetic_origin" value="" title="Genet_ori field should contain..." style="width : 92px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Segregation,ASC';document.forms[0].submit();">
                <TH>Segregation</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Segregation column" title="Hide Segregation column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Segregation';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Segregation" value="" title="Segregation field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Reference,ASC';document.forms[0].submit();">
                <TH>Reference</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Reference column" title="Hide Reference column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Reference';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Reference" value="" title="Reference field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Detection/Template,ASC';document.forms[0].submit();">
                <TH>Template</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Template column" title="Hide Template column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Detection/Template';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Detection/Template" value="" title="Template field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="200" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Detection/Technique,ASC';document.forms[0].submit();">
                <TH>Technique</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Technique column" title="Hide Technique column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Detection/Technique';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Detection/Technique" value="" title="Technique field should contain..." style="width : 192px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="90" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Frequency,ASC';document.forms[0].submit();">
                <TH>Frequency</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide Frequency column" title="Hide Frequency column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Frequency';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Frequency" value="" title="Frequency field should contain..." style="width : 82px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH>
          <TH valign="top" width="100" class="order"><IMG src="./gfx/trans.png" alt="" height="1"><BR>
            <TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="S11">
              <TR onclick="document.forms[0].order.value='Variant/Restriction_site,ASC';document.forms[0].submit();">
                <TH>RE-site</TH>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_hide.png" alt="Hide RE-site column" title="Hide RE-site column" width="11" height="11" onclick="document.forms[0].hide_col.value='Variant/Restriction_site';document.forms[0].submit();" style="margin : 1px;"></TD>
                <TD align="right" width="13"><IMG src="./gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="6"><BR><IMG src="./gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="6"></TD></TR>
              <TR>
                <TD colspan="3"><INPUT type="text" name="search_Variant/Restriction_site" value="" title="RE-site field should contain..." style="width : 92px; font-weight : normal;" onchange="document.forms[0].submit();" onkeydown="if (event.keyCode == 13) { document.forms[0].submit(); }"></TD></TR></TABLE></TH></TR></TABLE></DIV>
      <TABLE border="0" cellpadding="0" cellspacing="1" class="data" id="table_data">
        <TR>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD>
          <TD><IMG src="./gfx/trans.png" alt="" height="1"></TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.%28%3F_-301%29_309%2B%3Fdel';">
          <TD width="50">-</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.%28%3F_-301%29_309%2B%3Fdel" class="data">c.(?_-301)_309+?del</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.0?</TD>
          <TD width="200">p.0?</TD>
          <TD width="80">CAPN3_00447</TD>
          <TD width="200">exon 1 deletion</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">PCR</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-763C%3EG';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-763C%3EG" class="data">c.-763C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00177</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">1/76</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-719A%3ET';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-719A%3ET" class="data">c.-719A>T</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00176</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">4/76</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-552G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-552G%3EA" class="data">c.-552G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00262</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15733273" target="_blank">Todorova 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-408T%3EC';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-408T%3EC" class="data">c.-408T>C</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00049</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-322A%3EC';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-322A%3EC" class="data">c.-322A>C</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00175</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">2/76</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-104G%3EC';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.-104G%3EC" class="data">c.-104G>C</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.-104g>c</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00171</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">3/76</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.%3D';">
          <TD width="50">1_24</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.%3D" class="data">c.=</A><BR>&nbsp;&nbsp;(Reported 14 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.=</TD>
          <TD width="200">p.=</TD>
          <TD width="80">CAPN3_00000</TD>
          <TD width="200">no variants 2nd chromosome</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.%3F';">
          <TD width="50">1_24</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.%3F" class="data">c.?</A><BR>&nbsp;&nbsp;(Reported 14 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.?</TD>
          <TD width="200">p.?</TD>
          <TD width="80">CAPN3_00000</TD>
          <TD width="200">unknown variant 2nd allele</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.8C%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.8C%3EA" class="data">c.8C>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Thr3Asn)</TD>
          <TD width="80">CAPN3_00332</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.9C%3ET';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.9C%3ET" class="data">c.9C>T</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00050</TD>
          <TD width="200">determined on >100 chromosomes</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90"><0.01</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.10G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.10G%3EA" class="data">c.10G>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Val4Ile)</TD>
          <TD width="80">CAPN3_00051</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard 1999</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.19_23del';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.19_23del" class="data">c.19_23del</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ala7Cysfs*8)</TD>
          <TD width="80">CAPN3_00020</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/09150160" target="_blank">Richard 1997</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/09266733" target="_blank">Dincer 1997</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">HpaII-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.60delA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.60delA" class="data">c.60delA</A><BR>&nbsp;&nbsp;(Reported 6 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Pro22Glnfs*35)</TD>
          <TD width="80">CAPN3_00052</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">Ginjaar WMS2005</TD>
          <TD width="200">DNA</TD>
          <TD width="200">DGGE</TD>
          <TD width="90">-</TD>
          <TD width="100">BsrI+</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.62G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.62G%3EA" class="data">c.62G>A</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Gly21Glu)</TD>
          <TD width="80">CAPN3_00265</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.77C%3ET';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.77C%3ET" class="data">c.77C>T</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Pro26Leu)</TD>
          <TD width="80">CAPN3_00053</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">NlaIV-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.78G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.78G%3EA" class="data">c.78G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00513</TD>
          <TD width="200">from website <a href='http://genetics.emory.edu/egl/emvclass/emvclass.php'>Emory Genetics Lab</a></TD>
          <TD width="100">unknown</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.96T%3EC';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.96T%3EC" class="data">c.96T>C</A><BR>&nbsp;&nbsp;(Reported 12 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00061</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.100delG';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.100delG" class="data">c.100delG</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ala34fs*23)</TD>
          <TD width="80">CAPN3_00165</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15221789" target="_blank">Fanin 2004</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/16816913" target="_blank">Pizzanelli 2006</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.133G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.133G%3EA" class="data">c.133G>A</A><BR>&nbsp;&nbsp;(Reported 11 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.133g>a</TD>
          <TD width="200">p.Ala45Thr</TD>
          <TD width="80">CAPN3_00167</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15351423" target="_blank">Chrobakova</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/16372320" target="_blank">Hermanova 2005</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/17157502" target="_blank">Stehlikova 2006</A></TD>
          <TD width="200">DNA, RNA</TD>
          <TD width="200">RT-PCR, SEQ, DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.140_142del';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.140_142del" class="data">c.140_142del</A><BR>&nbsp;&nbsp;(Reported 11 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ile47del)</TD>
          <TD width="80">CAPN3_00193</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.143G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.143G%3EA" class="data">c.143G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ser48Asn)</TD>
          <TD width="80">CAPN3_00201</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15221789" target="_blank">Fanin 2004</A> + <A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.145C%3ET';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.145C%3ET" class="data">c.145C>T</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg49Cys)</TD>
          <TD width="80">CAPN3_00263</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/18055493" target="_blank">Groen 2007</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.146G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.146G%3EA" class="data">c.146G>A</A><BR>&nbsp;&nbsp;(Reported 7 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg49His)</TD>
          <TD width="80">CAPN3_00190</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/14981715" target="_blank">Canki-Klain</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/16100770" target="_blank">Milic 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">PCR</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.149A%3EG';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.149A%3EG" class="data">c.149A>G</A><BR>&nbsp;&nbsp;(Reported 5 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Asn50Ser)</TD>
          <TD width="80">CAPN3_00303</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.163G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.163G%3EA" class="data">c.163G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Gly55Arg)</TD>
          <TD width="80">CAPN3_00239</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.193C%3EG';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.193C%3EG" class="data">c.193C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(His65Asp)</TD>
          <TD width="80">CAPN3_00412</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/18055493" target="_blank">Groen 2007</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.206T%3EC';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.206T%3EC" class="data">c.206T>C</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Leu69Pro)</TD>
          <TD width="80">CAPN3_00312</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.224A%3EG';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.224A%3EG" class="data">c.224A>G</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.224a>g</TD>
          <TD width="200">p.Tyr75Cys</TD>
          <TD width="80">CAPN3_00371</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/17157502" target="_blank">Stehlikova 2006</A></TD>
          <TD width="200">DNA, RNA</TD>
          <TD width="200">RT-PCR, DHPLC, SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.225dupT';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.225dupT" class="data">c.225dupT</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Val76Cysfs*4)</TD>
          <TD width="80">CAPN3_00054</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.229G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.229G%3EA" class="data">c.229G>A</A><BR>&nbsp;&nbsp;(Reported 9 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Asp77Asn)</TD>
          <TD width="80">CAPN3_00056</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">Cfr10I-;NspBII+</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.232C%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.232C%3EA" class="data">c.232C>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Pro78Thr)</TD>
          <TD width="80">CAPN3_00444</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.240C%3EG';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.240C%3EG" class="data">c.240C>G</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Phe80Leu)</TD>
          <TD width="80">CAPN3_00429</TD>
          <TD width="200">control chromosomes</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/17994539" target="_blank">Guglieri 2007</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.245C%3ET';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.245C%3ET" class="data">c.245C>T</A><BR>&nbsp;&nbsp;(Reported 26 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Pro82Leu)</TD>
          <TD width="80">CAPN3_00143</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.246G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.246G%3EA" class="data">c.246G>A</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00379</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16650086" target="_blank">Krahn 2006</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.249_253del';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.249_253del" class="data">c.249_253del</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Glu84Leufs*5)</TD>
          <TD width="80">CAPN3_00192</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.257C%3ET';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.257C%3ET" class="data">c.257C>T</A><BR>&nbsp;&nbsp;(Reported 7 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.257c>u</TD>
          <TD width="200">p.Ser86Phe</TD>
          <TD width="80">CAPN3_00021</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/09150160" target="_blank">Richard 1997</A>, <A href="http://www.omim.org/entry/114240#0004" target="_blank">(OMIM 0004)</A></TD>
          <TD width="200">DNA, RNA</TD>
          <TD width="200">HD, RT-PCR, SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.258dupT';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.258dupT" class="data">c.258dupT</A><BR>&nbsp;&nbsp;(Reported 5 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Leu87Serfs*4)</TD>
          <TD width="80">CAPN3_00380</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16650086" target="_blank">Krahn 2006</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.259C%3EG';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.259C%3EG" class="data">c.259C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Leu87Val)</TD>
          <TD width="80">CAPN3_00219</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.260dupT';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.260dupT" class="data">c.260dupT</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(p.(Phe88Leufs*3)</TD>
          <TD width="80">CAPN3_00370</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15221789" target="_blank">Fanin 2004</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.260_265delinsGA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.260_265delinsGA" class="data">c.260_265delinsGA</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Leu87Argfs*39)</TD>
          <TD width="80">CAPN3_00144</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12461690" target="_blank">de Paula</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA, DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.277_300del';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.277_300del" class="data">c.277_300del</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Phe93_Lys100del)</TD>
          <TD width="80">CAPN3_00057</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.286delC';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.286delC" class="data">c.286delC</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Gln96Serfs*31)</TD>
          <TD width="80">CAPN3_00420</TD>
          <TD width="200">control chromosomes</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/17994539" target="_blank">Guglieri 2007</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.291C%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.291C%3EA" class="data">c.291C>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Phe97Leu)</TD>
          <TD width="80">CAPN3_00264</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.292G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.292G%3EA" class="data">c.292G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Val98Ile)</TD>
          <TD width="80">CAPN3_00240</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.294C%3EG';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.294C%3EG" class="data">c.294C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00514</TD>
          <TD width="200">from website <a href='http://genetics.emory.edu/egl/emvclass/emvclass.php'>Emory Genetics Lab</a></TD>
          <TD width="100">unknown</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.302G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.302G%3EA" class="data">c.302G>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg101Lys)</TD>
          <TD width="80">CAPN3_00317</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.304C%3ET';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.304C%3ET" class="data">c.304C>T</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Pro102Ser)</TD>
          <TD width="80">CAPN3_00220</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.308C%3ET';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.308C%3ET" class="data">c.308C>T</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Pro103Leu)</TD>
          <TD width="80">CAPN3_00221</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.309G%3EA';">
          <TD width="50">1</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.309G%3EA" class="data">c.309G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.0</TD>
          <TD width="200">p.0</TD>
          <TD width="80">CAPN3_00402</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA, RNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.309%2B1G%3ET';">
          <TD width="50">1i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.309%2B1G%3ET" class="data">c.309+1G>T</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.spl?</TD>
          <TD width="200">p.(?)</TD>
          <TD width="80">CAPN3_00122</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">Ginjaar WMS2005</TD>
          <TD width="200">DNA</TD>
          <TD width="200">DGGE</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.309%2B41G%3EA';">
          <TD width="50">1i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.309%2B41G%3EA" class="data">c.309+41G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00515</TD>
          <TD width="200">from website <a href='http://genetics.emory.edu/egl/emvclass/emvclass.php'>Emory Genetics Lab</a></TD>
          <TD width="100">unknown</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.309%2B4469_1116-1204del';">
          <TD width="50">1i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.309%2B4469_1116-1204del" class="data">c.309+4469_1116-1204del</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.[310_1115del, -52_269del;310_1115del]</TD>
          <TD width="200">p.[Glu104Metfs*11, 0?]</TD>
          <TD width="80">CAPN3_00295</TD>
          <TD width="200">custom-design NimbleGen array</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/17979987" target="_blank">Krahn 2007</A></TD>
          <TD width="200">DNA, RNA</TD>
          <TD width="200">arrayCGH, DHPLC, RT-PCR, SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.310-%3F_%28%2A544_%3F%29del';">
          <TD width="50">1i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.310-%3F_%28%2A544_%3F%29del" class="data">c.310-?_(*544_?)del</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(ex02ex24del)</TD>
          <TD width="200">p.?</TD>
          <TD width="80">CAPN3_00445</TD>
          <TD width="200">originally scored as homozygous</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">Ginjaar, WMS2008</TD>
          <TD width="200">DNA</TD>
          <TD width="200">MLPA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.310-%3F_945%2B%3Fdel';">
          <TD width="50">1i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.310-%3F_945%2B%3Fdel" class="data">c.310-?_945+?del</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(ex02ex06del)</TD>
          <TD width="200">p.?</TD>
          <TD width="80">CAPN3_00446</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">Ginjaar, WMS2008</TD>
          <TD width="200">DNA</TD>
          <TD width="200">MLPA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.310-%3F_1115%2B%3Fdel';">
          <TD width="50">1i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.310-%3F_1115%2B%3Fdel" class="data">c.310-?_1115+?del</A><BR>&nbsp;&nbsp;(Reported 7 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Glu104Metfs*11)</TD>
          <TD width="80">CAPN3_00173</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">Joncourt ESHG 2003, P0667</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.318C%3ET';">
          <TD width="50">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.318C%3ET" class="data">c.318C>T</A><BR>&nbsp;&nbsp;(Reported 7 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00058</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.319G%3EA';">
          <TD width="50">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.319G%3EA" class="data">c.319G>A</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Glu107Lys)</TD>
          <TD width="80">CAPN3_00059</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">Politano et al., Neuromuscul.Disord. 12: 733</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.327_328del';">
          <TD width="50">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.327_328del" class="data">c.327_328del</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg110Ilefs*4)</TD>
          <TD width="80">CAPN3_00266</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/18055493" target="_blank">Groen 2007</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.327_328dup';">
          <TD width="50">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.327_328dup" class="data">c.327_328dup</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg110Profs*18)</TD>
          <TD width="80">CAPN3_00440</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/18055493" target="_blank">Groen 2007</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.328C%3ET';">
          <TD width="50">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.328C%3ET" class="data">c.328C>T</A><BR>&nbsp;&nbsp;(Reported 18 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg110*)</TD>
          <TD width="80">CAPN3_00001</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/12461690" target="_blank">de Paula</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA, DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.332T%3EC';">
          <TD width="50">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.332T%3EC" class="data">c.332T>C</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Phe111Ser)</TD>
          <TD width="80">CAPN3_00318</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.352A%3EG';">
          <TD width="50">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.352A%3EG" class="data">c.352A>G</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg118Gly)</TD>
          <TD width="80">CAPN3_00060</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.358G%3EA';">
          <TD width="50">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.358G%3EA" class="data">c.358G>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Asp120Asn)</TD>
          <TD width="80">CAPN3_00319</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.363C%3EG';">
          <TD width="50">2</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.363C%3EG" class="data">c.363C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ile121Met)</TD>
          <TD width="80">CAPN3_00401</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.379%2B423T%3EA';">
          <TD width="50">2i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.379%2B423T%3EA" class="data">c.379+423T>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00507</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.379%2B432T%3EA';">
          <TD width="50">2i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.379%2B432T%3EA" class="data">c.379+432T>A</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00508</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.380-52T%3EG';">
          <TD width="50">2i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.380-52T%3EG" class="data">c.380-52T>G</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(=)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00174</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">1/76</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.380-27C%3ET';">
          <TD width="50">2i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.380-27C%3ET" class="data">c.380-27C>T</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(=)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00339</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/15689361" target="_blank">Saenz 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.380-2A%3EC';">
          <TD width="50">2i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.380-2A%3EC" class="data">c.380-2A>C</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.[380_498del, 379_380ins380-45_380-1; 380-2a>c]</TD>
          <TD width="200">p.[Gly127Valfs*14, Gly127_Asp128ins15]</TD>
          <TD width="80">CAPN3_00423</TD>
          <TD width="200">control chromosomes</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/17994539" target="_blank">Guglieri 2007</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.389G%3EC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.389G%3EC" class="data">c.389G>C</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.389g>c</TD>
          <TD width="200">p.Trp130Ser</TD>
          <TD width="80">CAPN3_00347</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/17897828" target="_blank">Lo 2008</A>, Tay WMS2006 P.P.6.04</TD>
          <TD width="200">DNA, RNA</TD>
          <TD width="200">RT-PCR, SEQ</TD>
          <TD width="90">?</TD>
          <TD width="100">?</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.390G%3EC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.390G%3EC" class="data">c.390G>C</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Trp130Cys)</TD>
          <TD width="80">CAPN3_00267</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.398C%3ET';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.398C%3ET" class="data">c.398C>T</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ala133Val)</TD>
          <TD width="80">CAPN3_00222</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.399A%3EG';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.399A%3EG" class="data">c.399A>G</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.399a>g</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00392</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">GenBank</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.402delC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.402delC" class="data">c.402delC</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.402del</TD>
          <TD width="200">p.Ile135Leufs*4</TD>
          <TD width="80">CAPN3_00022</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/09150160" target="_blank">Richard 1997</A></TD>
          <TD width="200">DNA, RNA</TD>
          <TD width="200">RT-PCR, SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.409T%3EC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.409T%3EC" class="data">c.409T>C</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Cys137Arg)</TD>
          <TD width="80">CAPN3_00063</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.413T%3EC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.413T%3EC" class="data">c.413T>C</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Leu138Pro)</TD>
          <TD width="80">CAPN3_00124</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">Ginjaar WMS2005</TD>
          <TD width="200">DNA</TD>
          <TD width="200">DGGE</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.416C%3ET';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.416C%3ET" class="data">c.416C>T</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Thr139Ile)</TD>
          <TD width="80">CAPN3_00320</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.418dupC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.418dupC" class="data">c.418dupC</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Leu140Profs*13)</TD>
          <TD width="80">CAPN3_00064</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.424C%3ET';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.424C%3ET" class="data">c.424C>T</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Gln142*)</TD>
          <TD width="80">CAPN3_00065</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard 1999</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.440G%3EA';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.440G%3EA" class="data">c.440G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg147Gln)</TD>
          <TD width="80">CAPN3_00450</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/17994539" target="_blank">Guglieri 2007</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.440G%3EC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.440G%3EC" class="data">c.440G>C</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg147Pro)</TD>
          <TD width="80">CAPN3_00142</TD>
          <TD width="200">control chromosomes</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10567047" target="_blank">Minami</A></TD>
          <TD width="200">DNA, RNA</TD>
          <TD width="200">RT-PCR, SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">BsrI+</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.477C%3ET';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.477C%3ET" class="data">c.477C>T</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00241</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.478G%3EC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.478G%3EC" class="data">c.478G>C</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ala160Pro)</TD>
          <TD width="80">CAPN3_00268</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.479C%3EA';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.479C%3EA" class="data">c.479C>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ala160Glu)</TD>
          <TD width="80">CAPN3_00321</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.479C%3EG';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.479C%3EG" class="data">c.479C>G</A><BR>&nbsp;&nbsp;(Reported 4 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ala160Gly)</TD>
          <TD width="80">CAPN3_00135</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">Politano et al., Neuromuscul.Disord. 12: 733</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.481G%3EA';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.481G%3EA" class="data">c.481G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Gly161Arg)</TD>
          <TD width="80">CAPN3_00462</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">PCR, SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.483delG';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.483delG" class="data">c.483delG</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ile162Serfs*17)</TD>
          <TD width="80">CAPN3_00382</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16650086" target="_blank">Krahn 2006</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.484A%3EC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.484A%3EC" class="data">c.484A>C</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Ile162Leu)</TD>
          <TD width="80">CAPN3_00066</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">AvaII-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.495C%3EG';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.495C%3EG" class="data">c.495C>G</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Phe165Leu)</TD>
          <TD width="80">CAPN3_00170</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.495C%3ET';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.495C%3ET" class="data">c.495C>T</A><BR>&nbsp;&nbsp;(Reported 10 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00067</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SEQ, SSCA</TD>
          <TD width="90">0.01</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.496delC';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.496delC" class="data">c.496delC</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(spl?)</TD>
          <TD width="200">p.(Gln166Serfs*13)</TD>
          <TD width="80">CAPN3_00139</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.498G%3EA';">
          <TD width="50">3</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.498G%3EA" class="data">c.498G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(spl?)</TD>
          <TD width="200">p.(?)</TD>
          <TD width="80">CAPN3_00068</TD>
          <TD width="200">determined on >100 chromosomes</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/10330340" target="_blank">Richard</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90"><0.01</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.498%2B1G%3EA';">
          <TD width="50">3i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.498%2B1G%3EA" class="data">c.498+1G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.spl?</TD>
          <TD width="200">p.(?)</TD>
          <TD width="80">CAPN3_00223</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.498%2B35G%3ET';">
          <TD width="50">3i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.498%2B35G%3ET" class="data">c.498+35G>T</A><BR>&nbsp;&nbsp;(Reported 5 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(spl?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00242</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC, SEQ</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.499-21G%3EC';">
          <TD width="50">3i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.499-21G%3EC" class="data">c.499-21G>C</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(?)</TD>
          <TD width="80">CAPN3_00333</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200">-</TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.499-17G%3EA';">
          <TD width="50">3i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.499-17G%3EA" class="data">c.499-17G>A</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(=)</TD>
          <TD width="80">CAPN3_00243</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16141003" target="_blank">Piluso 2005</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.499-1G%3EA';">
          <TD width="50">3i</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.499-1G%3EA" class="data">c.499-1G>A</A><BR>&nbsp;&nbsp;(Reported 3 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.spl?</TD>
          <TD width="200">p.(?)</TD>
          <TD width="80">CAPN3_00373</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16650086" target="_blank">Krahn 2006</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">DHPLC</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.502T%3EC';">
          <TD width="50">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.502T%3EC" class="data">c.502T>C</A></TD>
          <TD width="200">-</TD>
          <TD width="200">r.502u>c</TD>
          <TD width="200">p.Trp168Arg</TD>
          <TD width="80">CAPN3_00443</TD>
          <TD width="200">-</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/17897828" target="_blank">Lo 2008</A>, Tay WMS2006 P.P.6.04</TD>
          <TD width="200">DNA, RNA</TD>
          <TD width="200">RT-PCR, SEQ</TD>
          <TD width="90">?</TD>
          <TD width="100">?</TD></TR>
        <TR valign="top" style="cursor : pointer; cursor : hand;" onmouseover="this.className = 'hover';" onmouseout="this.className = '';" onclick="window.location.href = '/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.505C%3EG';">
          <TD width="50">4</TD>
          <TD width="200" class="ordered"><A href="/nmdb2/variants.php?select_db=CAPN3&amp;action=search_all&amp;search_Variant%2FDNA=c.505C%3EG" class="data">c.505C>G</A><BR>&nbsp;&nbsp;(Reported 2 times)</TD>
          <TD width="200">-</TD>
          <TD width="200">r.(?)</TD>
          <TD width="200">p.(Arg169Gly)</TD>
          <TD width="80">CAPN3_00184</TD>
          <TD width="200">control chromosomes</TD>
          <TD width="100">germline (inherited)</TD>
          <TD width="200">-</TD>
          <TD width="200"><A href="http://www.ncbi.nlm.nih.gov/pubmed/16001438" target="_blank">Georgieva 2005</A>, <A href="http://www.ncbi.nlm.nih.gov/pubmed/17318636" target="_blank">Todorova 2007</A></TD>
          <TD width="200">DNA</TD>
          <TD width="200">SSCA</TD>
          <TD width="90">-</TD>
          <TD width="100">-</TD></TR></TABLE>
</FORM>

      <SPAN class="S11">
      1 - 100
      <BR>
 [&lt;-]  <B>1</B>  <A href="/nmdb2/variants.php?action=search_unique&amp;limit=100&amp;order=Variant%2FDNA%2CASC&amp;page=2">2</A>  <A href="/nmdb2/variants.php?action=search_unique&amp;limit=100&amp;order=Variant%2FDNA%2CASC&amp;page=3">3</A>  <A href="/nmdb2/variants.php?action=search_unique&amp;limit=100&amp;order=Variant%2FDNA%2CASC&amp;page=4">4</A>  <A href="/nmdb2/variants.php?action=search_unique&amp;limit=100&amp;order=Variant%2FDNA%2CASC&amp;page=5">5</A>  [<A href="/nmdb2/variants.php?action=search_unique&amp;limit=100&amp;order=Variant%2FDNA%2CASC&amp;page=2">-&gt;</A>]      </SPAN><BR>
      <BR>

      <SPAN class="S15"><B>Legend:</B></SPAN> [ <A href="variants_legend.php?select_db=CAPN3" target="_blank">CAPN3 full legend</A> ]<BR>

      <SPAN class="S11">
        Sequence variations are described basically as recommended by the Ad-Hoc Committee for Mutation Nomenclature (AHCMN), with the recently suggested additions (den Dunnen JT and Antonarakis SE [2000], Hum.Mut. 15:7-12); for a summary see <A href="http://www.HGVS.org/mutnomen/"><B>Nomenclature</B></A>.
        <A href="http://www.dmd.nl/nmdb2/refseq/CAPN3_codingDNA.html">Coding DNA Reference Sequence</A>, with the first base of the Met-codon counted as position 1.<BR>
        <B>Exon:</B> number of exon/intron containing variant <B>DNA change:</B> DNA change <B>Var_pub_as:</B> Var_pub_as <B>RNA change:</B> RNA change <B>Protein change:</B> Protein change <B>CAPN3 DB-ID:</B> DB-ID <B>Variant remarks:</B> Variant remarks <B>Genet_ori:</B> origin of variant; unknown, germline (i.e. inherited), somatic, de novo, from parental disomy (maternal or paternal) or in vitro (cloned) <B>Segregation:</B> indicates whether the variant segregates with the disease (yes), does not segregate with the disease (no) or segregation is unknown (?) <B>Reference:</B> publication describing the variant submitted, incl. links to OMIM and dbSNP (when available) <B>Template:</B> Template <B>Technique:</B> Technique <B>Frequency:</B> Frequency <B>RE-site:</B> RE-site</SPAN><BR><BR>









    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/2.0/" target="_blank">LOVD v.2.0</A> Build 35<BR>
  Enabled modules: recaptcha, showmaxdbid, mutalyzer<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="./gfx/lovd_update_newest_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>

<SCRIPT type="text/javascript">
  <!--
  objImg = document.getElementById('mapping_progress');

function lovd_HTTPRequest (sURL) {
    // Create HTTP request object.
    var objHTTP;
    try {
        // W3C standard.
        objHTTP = new XMLHttpRequest();
    } catch (e) {
        // Internet Explorer?
        try {
            objHTTP = new ActiveXObject("Msxml2.XMLHTTP");
        } catch (e) {
            try {
                objHTTP = new ActiveXObject("Microsoft.XMLHTTP");
            } catch (e) {
                // Ok, last try!
                try {
                    objHTTP = window.createRequest();
                } catch (e) {
                    // Never mind.
                    objHTTP = false;
                }
            }
        }
    }

    if (objHTTP) {
        objHTTP.open("GET", sURL, false);
        objHTTP.send(null);
        return objHTTP;

    } else {
        return false;
    }
}



  function lovd_mapVariants () {
    // Request file that will do the actual work.
    objHTTP = lovd_HTTPRequest("http://www.dmd.nl/nmdb2/ajax-map_variants.php");

    if (!objHTTP || objHTTP.status != 200) {
        // Don't try again.
        objImg.src = "./gfx/lovd_mapping_99.png";
        objImg.title = "There was a problem with LOVD while mapping variants to the genome.";
    } else {
        aResponse = objHTTP.responseText.split("\t");
        // 2010-05-03; 2.0-26; Verify output, to prevent PHP errors from freaking out the browser (= every 50 microseconds a new request).
        // Took (and shortened) the "is_numeric()" implementation from http://phpjs.org/functions/is_numeric:449 (thanks guys).
        if (aResponse.length == 2 && !isNaN(aResponse[0])) {
            objImg.src = "./gfx/lovd_mapping_" + aResponse[0] + ".png";
            objImg.title = aResponse[1];

            if (aResponse[1] != "All done!") {
                setTimeout("lovd_mapVariants()", 50);
            } else {
                objImg.setAttribute("onclick", "lovd_mapVariants();");
            }
        } else {
            objImg.title = "Error occured: " + objHTTP.responseText;
        }
    }
  }

objImg.setAttribute("onclick", "lovd_mapVariants();");
  // -->
</SCRIPT>

<SCRIPT type="text/javascript" src="./inc-js-sticky_header.js"></SCRIPT>
</BODY></HTML>"""

CAPN3_TABLE_DATA = [['-', 'NM_000070.2:c.(?_-301)_309+?del', '-', 'r.0?', 'p.0?', 'CAPN3_00447', 'exon 1 deletion', 'germline (inherited)', '-', '-', 'DNA', 'PCR', '-', '-'], ['1', 'NM_000070.2:c.-763C>G', '-', 'r.(?)', 'p.(=)', 'CAPN3_00177', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '1/76', '-'], ['1', 'NM_000070.2:c.-719A>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00176', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '4/76', '-'], ['1', 'NM_000070.2:c.-552G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00262', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15733273', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.-408T>C', '-', 'r.(?)', 'p.(=)', 'CAPN3_00049', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-'], ['1', 'NM_000070.2:c.-322A>C', '-', 'r.(?)', 'p.(=)', 'CAPN3_00175', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '2/76', '-'], ['1', 'NM_000070.2:c.-104G>C', '-', 'r.-104g>c', 'p.(=)', 'CAPN3_00171', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '3/76', '-'], ['1_24', 'NM_000070.2:c.=', '-', 'r.=', 'p.=', 'CAPN3_00000', 'no variants 2nd chromosome', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1_24', 'NM_000070.2:c.?', '-', 'r.?', 'p.?', 'CAPN3_00000', 'unknown variant 2nd allele', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.8C>A', '-', 'r.(?)', 'p.(Thr3Asn)', 'CAPN3_00332', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['1', 'NM_000070.2:c.9C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00050', 'determined on >100 chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '<0.01', '-'], ['1', 'NM_000070.2:c.10G>A', '-', 'r.(?)', 'p.(Val4Ile)', 'CAPN3_00051', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-'], ['1', 'NM_000070.2:c.19_23del', '-', 'r.(?)', 'p.(Ala7Cysfs*8)', 'CAPN3_00020', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09150160,http://www.ncbi.nlm.nih.gov/pubmed/09266733', 'DNA', 'SEQ', '-', 'HpaII-'], ['1', 'NM_000070.2:c.60delA', '-', 'r.(?)', 'p.(Pro22Glnfs*35)', 'CAPN3_00052', '-', 'germline (inherited)', '-', 'Ginjaar WMS2005', 'DNA', 'DGGE', '-', 'BsrI+'], ['1', 'NM_000070.2:c.62G>A', '-', 'r.(?)', 'p.(Gly21Glu)', 'CAPN3_00265', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.77C>T', '-', 'r.(?)', 'p.(Pro26Leu)', 'CAPN3_00053', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', 'NlaIV-'], ['1', 'NM_000070.2:c.78G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00513', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.96T>C', '-', 'r.(?)', 'p.(=)', 'CAPN3_00061', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.100delG', '-', 'r.(?)', 'p.(Ala34fs*23)', 'CAPN3_00165', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789,http://www.ncbi.nlm.nih.gov/pubmed/16816913', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.133G>A', '-', 'r.133g>a', 'p.Ala45Thr', 'CAPN3_00167', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15351423,http://www.ncbi.nlm.nih.gov/pubmed/16372320,http://www.ncbi.nlm.nih.gov/pubmed/17157502', 'DNA, RNA', 'RT-PCR, SEQ, DHPLC', '-', '-'], ['1', 'NM_000070.2:c.140_142del', '-', 'r.(?)', 'p.(Ile47del)', 'CAPN3_00193', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['1', 'NM_000070.2:c.143G>A', '-', 'r.(?)', 'p.(Ser48Asn)', 'CAPN3_00201', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789,http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.145C>T', '-', 'r.(?)', 'p.(Arg49Cys)', 'CAPN3_00263', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.146G>A', '-', 'r.(?)', 'p.(Arg49His)', 'CAPN3_00190', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/14981715,http://www.ncbi.nlm.nih.gov/pubmed/16100770', 'DNA', 'PCR', '-', '-'], ['1', 'NM_000070.2:c.149A>G', '-', 'r.(?)', 'p.(Asn50Ser)', 'CAPN3_00303', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['1', 'NM_000070.2:c.163G>A', '-', 'r.(?)', 'p.(Gly55Arg)', 'CAPN3_00239', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.193C>G', '-', 'r.(?)', 'p.(His65Asp)', 'CAPN3_00412', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.206T>C', '-', 'r.(?)', 'p.(Leu69Pro)', 'CAPN3_00312', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['1', 'NM_000070.2:c.224A>G', '-', 'r.224a>g', 'p.Tyr75Cys', 'CAPN3_00371', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17157502', 'DNA, RNA', 'RT-PCR, DHPLC, SEQ', '-', '-'], ['1', 'NM_000070.2:c.225dupT', '-', 'r.(?)', 'p.(Val76Cysfs*4)', 'CAPN3_00054', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.229G>A', '-', 'r.(?)', 'p.(Asp77Asn)', 'CAPN3_00056', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', 'Cfr10I-;NspBII+'], ['1', 'NM_000070.2:c.232C>A', '-', 'r.(?)', 'p.(Pro78Thr)', 'CAPN3_00444', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.240C>G', '-', 'r.(?)', 'p.(Phe80Leu)', 'CAPN3_00429', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.245C>T', '-', 'r.(?)', 'p.(Pro82Leu)', 'CAPN3_00143', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.246G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00379', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.249_253del', '-', 'r.(?)', 'p.(Glu84Leufs*5)', 'CAPN3_00192', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.257C>T', '-', 'r.257c>u', 'p.Ser86Phe', 'CAPN3_00021', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09150160,http://www.omim.org/entry/114240#0004', 'DNA, RNA', 'HD, RT-PCR, SEQ', '-', '-'], ['1', 'NM_000070.2:c.258dupT', '-', 'r.(?)', 'p.(Leu87Serfs*4)', 'CAPN3_00380', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.259C>G', '-', 'r.(?)', 'p.(Leu87Val)', 'CAPN3_00219', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.260dupT', '-', 'r.(?)', 'p.(p.(Phe88Leufs*3)', 'CAPN3_00370', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.260_265delinsGA', '-', 'r.(?)', 'p.(Leu87Argfs*39)', 'CAPN3_00144', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/12461690', 'DNA', 'SSCA, DHPLC', '-', '-'], ['1', 'NM_000070.2:c.277_300del', '-', 'r.(?)', 'p.(Phe93_Lys100del)', 'CAPN3_00057', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.286delC', '-', 'r.(?)', 'p.(Gln96Serfs*31)', 'CAPN3_00420', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.291C>A', '-', 'r.(?)', 'p.(Phe97Leu)', 'CAPN3_00264', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.292G>A', '-', 'r.(?)', 'p.(Val98Ile)', 'CAPN3_00240', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.294C>G', '-', 'r.(?)', 'p.(=)', 'CAPN3_00514', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1', 'NM_000070.2:c.302G>A', '-', 'r.(?)', 'p.(Arg101Lys)', 'CAPN3_00317', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['1', 'NM_000070.2:c.304C>T', '-', 'r.(?)', 'p.(Pro102Ser)', 'CAPN3_00220', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.308C>T', '-', 'r.(?)', 'p.(Pro103Leu)', 'CAPN3_00221', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['1', 'NM_000070.2:c.309G>A', '-', 'r.0', 'p.0', 'CAPN3_00402', '-', 'germline (inherited)', '-', '-', 'DNA, RNA', 'SEQ', '-', '-'], ['1i', 'NM_000070.2:c.309+1G>T', '-', 'r.spl?', 'p.(?)', 'CAPN3_00122', '-', 'germline (inherited)', '-', 'Ginjaar WMS2005', 'DNA', 'DGGE', '-', '-'], ['1i', 'NM_000070.2:c.309+41G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00515', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['1i', 'NM_000070.2:c.309+4469_1116-1204del', '-', 'r.[310_1115del, -52_269del;310_1115del]', 'p.[Glu104Metfs*11, 0?]', 'CAPN3_00295', 'custom-design NimbleGen array', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17979987', 'DNA, RNA', 'arrayCGH, DHPLC, RT-PCR, SEQ', '-', '-'], ['1i', 'NM_000070.2:c.310-?_(*544_?)del', '-', 'r.(ex02ex24del)', 'p.?', 'CAPN3_00445', 'originally scored as homozygous', 'germline (inherited)', '-', 'Ginjaar, WMS2008', 'DNA', 'MLPA', '-', '-'], ['1i', 'NM_000070.2:c.310-?_945+?del', '-', 'r.(ex02ex06del)', 'p.?', 'CAPN3_00446', '-', 'germline (inherited)', '-', 'Ginjaar, WMS2008', 'DNA', 'MLPA', '-', '-'], ['1i', 'NM_000070.2:c.310-?_1115+?del', '-', 'r.(?)', 'p.(Glu104Metfs*11)', 'CAPN3_00173', '-', 'germline (inherited)', '-', 'Joncourt ESHG 2003, P0667', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_000070.2:c.318C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00058', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_000070.2:c.319G>A', '-', 'r.(?)', 'p.(Glu107Lys)', 'CAPN3_00059', '-', 'germline (inherited)', '-', 'Politano et al., Neuromuscul.Disord. 12: 733', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_000070.2:c.327_328del', '-', 'r.(?)', 'p.(Arg110Ilefs*4)', 'CAPN3_00266', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_000070.2:c.327_328dup', '-', 'r.(?)', 'p.(Arg110Profs*18)', 'CAPN3_00440', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_000070.2:c.328C>T', '-', 'r.(?)', 'p.(Arg110*)', 'CAPN3_00001', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/12461690', 'DNA', 'SSCA, DHPLC', '-', '-'], ['2', 'NM_000070.2:c.332T>C', '-', 'r.(?)', 'p.(Phe111Ser)', 'CAPN3_00318', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['2', 'NM_000070.2:c.352A>G', '-', 'r.(?)', 'p.(Arg118Gly)', 'CAPN3_00060', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['2', 'NM_000070.2:c.358G>A', '-', 'r.(?)', 'p.(Asp120Asn)', 'CAPN3_00319', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['2', 'NM_000070.2:c.363C>G', '-', 'r.(?)', 'p.(Ile121Met)', 'CAPN3_00401', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['2i', 'NM_000070.2:c.379+423T>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00507', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['2i', 'NM_000070.2:c.379+432T>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00508', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['2i', 'NM_000070.2:c.380-52T>G', '-', 'r.(=)', 'p.(=)', 'CAPN3_00174', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '1/76', '-'], ['2i', 'NM_000070.2:c.380-27C>T', '-', 'r.(=)', 'p.(=)', 'CAPN3_00339', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15689361', 'DNA', 'SEQ', '-', '-'], ['2i', 'NM_000070.2:c.380-2A>C', '-', 'r.[380_498del, 379_380ins380-45_380-1; 380-2a>c]', 'p.[Gly127Valfs*14, Gly127_Asp128ins15]', 'CAPN3_00423', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_000070.2:c.389G>C', '-', 'r.389g>c', 'p.Trp130Ser', 'CAPN3_00347', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17897828', 'DNA, RNA', 'RT-PCR, SEQ', '?', '?'], ['3', 'NM_000070.2:c.390G>C', '-', 'r.(?)', 'p.(Trp130Cys)', 'CAPN3_00267', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_000070.2:c.398C>T', '-', 'r.(?)', 'p.(Ala133Val)', 'CAPN3_00222', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['3', 'NM_000070.2:c.399A>G', '-', 'r.399a>g', 'p.(=)', 'CAPN3_00392', '-', 'germline (inherited)', '-', 'GenBank', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_000070.2:c.402delC', '-', 'r.402del', 'p.Ile135Leufs*4', 'CAPN3_00022', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09150160', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['3', 'NM_000070.2:c.409T>C', '-', 'r.(?)', 'p.(Cys137Arg)', 'CAPN3_00063', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_000070.2:c.413T>C', '-', 'r.(?)', 'p.(Leu138Pro)', 'CAPN3_00124', '-', 'germline (inherited)', '-', 'Ginjaar WMS2005', 'DNA', 'DGGE', '-', '-'], ['3', 'NM_000070.2:c.416C>T', '-', 'r.(?)', 'p.(Thr139Ile)', 'CAPN3_00320', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['3', 'NM_000070.2:c.418dupC', '-', 'r.(?)', 'p.(Leu140Profs*13)', 'CAPN3_00064', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_000070.2:c.424C>T', '-', 'r.(?)', 'p.(Gln142*)', 'CAPN3_00065', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-'], ['3', 'NM_000070.2:c.440G>A', '-', 'r.(?)', 'p.(Arg147Gln)', 'CAPN3_00450', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_000070.2:c.440G>C', '-', 'r.(?)', 'p.(Arg147Pro)', 'CAPN3_00142', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10567047', 'DNA, RNA', 'RT-PCR, SEQ', '-', 'BsrI+'], ['3', 'NM_000070.2:c.477C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00241', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['3', 'NM_000070.2:c.478G>C', '-', 'r.(?)', 'p.(Ala160Pro)', 'CAPN3_00268', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_000070.2:c.479C>A', '-', 'r.(?)', 'p.(Ala160Glu)', 'CAPN3_00321', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['3', 'NM_000070.2:c.479C>G', '-', 'r.(?)', 'p.(Ala160Gly)', 'CAPN3_00135', '-', 'germline (inherited)', '-', 'Politano et al., Neuromuscul.Disord. 12: 733', 'DNA', 'SEQ', '-', '-'], ['3', 'NM_000070.2:c.481G>A', '-', 'r.(?)', 'p.(Gly161Arg)', 'CAPN3_00462', '-', 'germline (inherited)', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['3', 'NM_000070.2:c.483delG', '-', 'r.(?)', 'p.(Ile162Serfs*17)', 'CAPN3_00382', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['3', 'NM_000070.2:c.484A>C', '-', 'r.(?)', 'p.(Ile162Leu)', 'CAPN3_00066', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', 'AvaII-'], ['3', 'NM_000070.2:c.495C>G', '-', 'r.(?)', 'p.(Phe165Leu)', 'CAPN3_00170', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '-', '-'], ['3', 'NM_000070.2:c.495C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00067', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ, SSCA', '0.01', '-'], ['3', 'NM_000070.2:c.496delC', '-', 'r.(spl?)', 'p.(Gln166Serfs*13)', 'CAPN3_00139', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['3', 'NM_000070.2:c.498G>A', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00068', 'determined on >100 chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '<0.01', '-'], ['3i', 'NM_000070.2:c.498+1G>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00223', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['3i', 'NM_000070.2:c.498+35G>T', '-', 'r.(spl?)', 'p.(=)', 'CAPN3_00242', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC, SEQ', '-', '-'], ['3i', 'NM_000070.2:c.499-21G>C', '-', 'r.(?)', 'p.(?)', 'CAPN3_00333', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['3i', 'NM_000070.2:c.499-17G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00243', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['3i', 'NM_000070.2:c.499-1G>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00373', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['4', 'NM_000070.2:c.502T>C', '-', 'r.502u>c', 'p.Trp168Arg', 'CAPN3_00443', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17897828', 'DNA, RNA', 'RT-PCR, SEQ', '?', '?'], ['4', 'NM_000070.2:c.505C>G', '-', 'r.(?)', 'p.(Arg169Gly)', 'CAPN3_00184', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16001438,http://www.ncbi.nlm.nih.gov/pubmed/17318636', 'DNA', 'SSCA', '-', '-'], ['4', 'NM_000070.2:c.505C>T', '-', 'r.(?)', 'p.(Arg169Cys)', 'CAPN3_00353', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.506G>A', '-', 'r.(?)', 'p.(Arg169His)', 'CAPN3_00448', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.509A>G', '-', 'r.(?)', 'p.(Tyr170Cys)', 'CAPN3_00439', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.509dupA', '-', 'r.(?)', 'p.(Tyr170*)', 'CAPN3_00145', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/12461690', 'DNA', 'SSCA, DHPLC', '-', '-'], ['4', 'NM_000070.2:c.510T>G', '-', 'r.(?)', 'p.(Tyr170*)', 'CAPN3_00354', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.527T>C', '-', 'r.(?)', 'p.(Val176Ala)', 'CAPN3_00500', '-', 'germline (inherited)', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['4', 'NM_000070.2:c.533T>C', '-', 'r.(?)', 'p.(Ile178Thr)', 'CAPN3_00386', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['4', 'NM_000070.2:c.535G>C', '-', 'r.(?)', 'p.(Asp179His)', 'CAPN3_00428', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.539A>C', '-', 'r.(?)', 'p.(Asp180Ala)', 'CAPN3_00259', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15725583', 'DNA', 'DHPLC', '-', '-'], ['4', 'NM_000070.2:c.545T>A', '-', 'r.(?)', 'p.(Leu182Gln)', 'CAPN3_00002', 'not in 120 control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/07720071', 'DNA', 'HD, SEQ', '-', '-'], ['4', 'NM_000070.2:c.548C>G', '-', 'r.(?)', 'p.(Pro183Arg)', 'CAPN3_00224', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['4', 'NM_000070.2:c.548C>T', '-', 'r.(?)', 'p.(Pro183Leu)', 'CAPN3_00069', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.(550delA)?', '-', 'r.550del', 'p.Thr184Argfs*36', 'CAPN3_00010', '-', 'germline (inherited)', '-', '-', 'RNA', 'RT-PCR, SEQ', '-', '-'], ['4', 'NM_000070.2:c.550delA', '-', 'r.(?)', 'p.(Thr184Argfs*36\xc2\xa0)', 'CAPN3_00010', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.551C>T', '-', 'r.(?)', 'p.(Thr184Met)', 'CAPN3_00030', 'not in 120 control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340,http://www.ncbi.nlm.nih.gov/pubmed/9655129', 'DNA, RNA', 'HD, SEQ', '-', 'MboI-'], ['4', 'NM_000070.2:c.565C>G', '-', 'r.(?)', 'p.(Leu189Val)', 'CAPN3_00120', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11296367', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.566T>C', '-', 'r.(?)', 'p.(Leu189Pro)', 'CAPN3_00071', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.575C>T', '-', 'r.(?)', 'p.(Thr192Ile)', 'CAPN3_00260', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['4', 'NM_000070.2:c.580delT', '-', 'r.(?)', 'p.(Ser194Profs*26)', 'CAPN3_00526', '-', 'germline (inherited)', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['4', 'NM_000070.2:c.581C>G', '-', 'r.(?)', 'p.(Ser194Cys)', 'CAPN3_00322', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['4', 'NM_000070.2:c.590G>A', '-', 'r.(?)', 'p.(Arg197His)', 'CAPN3_00226', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789,http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['4', 'NM_000070.2:c.590G>T', '-', 'r.(?)', 'p.(Arg197Leu)', 'CAPN3_00323', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['4', 'NM_000070.2:c.593A>G', '-', 'r.(?)', 'p.(Asn198Ser)', 'CAPN3_00383', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['4', 'NM_000070.2:c.595G>C', '-', 'r.(?)', 'p.(Glu199Gln)', 'CAPN3_00438', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.598_612del', '-', 'r.(?)', 'p.(Phe200_Leu204del)', 'CAPN3_00025', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.601T>A', '-', 'r.(?)', 'p.(Trp201Arg)', 'CAPN3_00269', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.606T>C', '-', 'r.(?)', 'p.(=)', 'CAPN3_00238', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.610C>G', '-', 'r.(?)', 'p.(Leu204Val)', 'CAPN3_00408', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['4', 'NM_000070.2:c.616delG', '-', 'r.(?)', 'p.(Glu206Argfs*14)', 'CAPN3_00270', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.616G>A', '-', 'r.616g>a', 'p.Glu206Lys', 'CAPN3_00403', '-', 'germline (inherited)', '-', '-', 'DNA, RNA', 'SEQ', '-', '-'], ['4', 'NM_000070.2:c.(619_621del)?', '-', 'r.619_621del', 'p.Lys207del', 'CAPN3_00348', '-', 'germline (inherited)', '-', '-', 'RNA', 'RT-PCR, SEQ', '-', '-'], ['4', 'NM_000070.2:c.620A>C', '-', 'r.(?)', 'p.(Lys207Thr)', 'CAPN3_00227', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['4', 'NM_000070.2:c.631A>G', '-', 'r.(spl?)', 'p.(Lys211Glu)', 'CAPN3_00146', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/12461690', 'DNA', 'SSCA, DHPLC', '-', '-'], ['4i', 'NM_000070.2:c.632+1G>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00178', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '-', '-'], ['4i', 'NM_000070.2:c.632+1G>C', '-', 'r.spl?', 'p.(?)', 'CAPN3_00324', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['4i', 'NM_000070.2:c.632+3A>G', '-', 'r.spl?', 'p.(?)', 'CAPN3_00126', '-', 'germline (inherited)', '-', 'Ginjaar, Neuromuscul.Disord. 12:731,', 'DNA', 'DGGE, SEQ', '-', '-'], ['4i', 'NM_000070.2:c.632+4A>G', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00325', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['4i', 'NM_000070.2:c.632+404_1029+?del', '-', 'r.(?)', 'p.(?)', 'CAPN3_00073', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.633G>C', '-', 'r.(spl?)', 'p.(Lys211Asn?)', 'CAPN3_00437', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.633G>T', '-', 'r.(spl?)', 'p.(Lys211Asn?)', 'CAPN3_00228', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.635T>C', '-', 'r.(?)', 'p.(Leu212Pro)', 'CAPN3_00516', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.637C>T', '-', 'r.(?)', 'p.(His213Tyr)', 'CAPN3_00338', 'control chromosomes', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.638A>G', '-', 'r.(?)', 'p.(His213Arg)', 'CAPN3_00326', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.640G>A', '-', 'r.(?)', 'p.(Gly214Ser)', 'CAPN3_00074', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.643T>C', '-', 'r.(?)', 'p.(Ser215Pro)', 'CAPN3_00044', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09150160', 'DNA', 'SEQ', '-', 'BsrI+'], ['5', 'NM_000070.2:c.643_663del', '-', 'r.(?)', 'p.(Ser215_Gly221del)', 'CAPN3_00075', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09150160', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.649G>A', '-', 'r.(?)', 'p.(Glu217Lys)', 'CAPN3_00076', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.662G>T', '-', 'r.(?)', 'p.(Gly221Val)', 'CAPN3_00421', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.664G>A', '-', 'r.(?)', 'p.(Gly222Arg)', 'CAPN3_00027', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/9762961', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.674C>G', '-', 'r.(?)', 'p.(Thr225Arg)', 'CAPN3_00229', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.676G>A', '-', 'r.(?)', 'p.(Glu226Lys)', 'CAPN3_00078', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.689A>G', '-', 'r.(?)', 'p.(Asp230Gly)', 'CAPN3_00230', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.695C>T', '-', 'r.(?)', 'p.(Thr232Ile)', 'CAPN3_00080', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.697G>C', '-', 'r.(?)', 'p.(Gly233Arg)', 'CAPN3_00160', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.698G>T', '-', 'r.698g>u', 'p.Gly233Val', 'CAPN3_00150', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11525884', 'DNA, RNA', 'RT-PCR, SEQ', '-', 'ScaI+'], ['5', 'NM_000070.2:c.701G>A', '-', 'r.(?)', 'p.(Gly234Glu)', 'CAPN3_00003', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.703delG', '-', 'r.(?)', 'p.(Val235Trpfs*18)', 'CAPN3_00327', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.706G>A', '-', 'r.(?)', 'p.(Ala236Thr)', 'CAPN3_00082', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', 'ItaI'], ['5', 'NM_000070.2:c.717delT', '-', 'r.(?)', 'p.(Phe239Leufs*14)', 'CAPN3_00029', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.717dupT', '-', 'r.(?)', 'p.(Glu240*)', 'CAPN3_00271', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.724dupA', '-', 'r.(?)', 'p.(Arg242Lysfs*5)', 'CAPN3_00272', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.739G>A', '-', 'r.(?)', 'p.(Asp247Asn)', 'CAPN3_00231', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.743T>G', '-', 'r.(?)', 'p.(Met248Arg)', 'CAPN3_00147', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/12461690', 'DNA', 'SSCA, DHPLC', '-', 'AvaII-'], ['5', 'NM_000070.2:c.747C>G', '-', 'r.(?)', 'p.(Tyr249*)', 'CAPN3_00409', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.755T>A', '-', 'r.(?)', 'p.(Met252Lys)', 'CAPN3_00194', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.755T>C', '-', 'r.(?)', 'p.(Met252Thr)', 'CAPN3_00233', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.755T>G', '-', 'r.(?)', 'p.(Met252Arg)', 'CAPN3_00164', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.759_761del', '-', 'r.(?)', 'p.(Lys254del)', 'CAPN3_00055', '-', 'germline (inherited)', '-', 'Ginjaar WMS2005', 'DNA', 'DGGE', '-', 'MspI'], ['5', 'NM_000070.2:c.760A>G', '-', 'r.(?)', 'p.(Lys254Glu)', 'CAPN3_00400', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.763G>C', '-', 'r.(?)', 'p.(Ala255Pro)', 'CAPN3_00328', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.769G>T', '-', 'r.(?)', 'p.(Glu257*)', 'CAPN3_00329', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.779C>T', '-', 'r.(?)', 'p.(Ser260Phe)', 'CAPN3_00330', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['5', 'NM_000070.2:c.788G>A', '-', 'r.(?)', 'p.(Gly263Asp)', 'CAPN3_00273', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['5', 'NM_000070.2:c.791G>A', '-', 'r.(?)', 'p.(Cys264Tyr)', 'CAPN3_00375', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['5', 'NM_000070.2:c.798T>C', '-', 'r.(?)', 'p.(=)', 'CAPN3_00244', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['5i', 'NM_000070.2:c.801+1G>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00026', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['5i', 'NM_000070.2:c.802-9G>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00203', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['5i', 'NM_000070.2:c.802-?_945+?del', '802_945del', 'r.(del)', 'p.(del)', 'CAPN3_00451', '-', 'germline (inherited)', '-', 'ESHG2010, Stehlikova P12.117', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_000070.2:c.817A>G', '-', 'r.817a>g', 'p.(Thr273Ala)', 'CAPN3_00393', '-', 'germline (inherited)', '-', 'GenBank', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_000070.2:c.822T>G', '-', 'r.(?)', 'p.(Tyr274*)', 'CAPN3_00501', '-', 'germline (inherited)', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['6', 'NM_000070.2:c.847A>G', '-', 'r.(?)', 'p.(Met283Val)', 'CAPN3_00506', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_000070.2:c.848T>C', '-', 'r.(?)', 'p.(Met283Thr)', 'CAPN3_00390', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['6', 'NM_000070.2:c.865C>T', '-', 'r.(?)', 'p.(Arg289Trp)', 'CAPN3_00172', '-', 'germline (inherited)', '-', '-', 'DNA', 'DGGE', '-', '-'], ['6', 'NM_000070.2:c.883_886delinsCTT', '-', 'r.(?)', 'p.(Asp295Leufs*57)', 'CAPN3_00234', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['6', 'NM_000070.2:c.887delA', '-', 'r.(?)', 'p.(Asn296Thrfs*56)', 'CAPN3_00083', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_000070.2:c.898C>T', '-', 'r.(?)', 'p.(Gln300*)', 'CAPN3_00331', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['6', 'NM_000070.2:c.943C>T', '-', 'r.(?)', 'p.(Arg315Trp)', 'CAPN3_00517', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['6', 'NM_000070.2:c.945+1delG', '945delG', 'r.(spl?)', 'p.(del?)', 'CAPN3_00005', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/07720071', 'DNA', 'HD, SEQ', '-', 'SmaI-'], ['6i', 'NM_000070.2:c.945+5G>A', '-', 'r.spl?', 'p.?', 'CAPN3_00245', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['6i', 'NM_000070.2:c.945+14C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00246', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['6i', 'NM_000070.2:c.945+56C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00247', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['6i', 'NM_000070.2:c.945+91C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00248', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['6i', 'NM_000070.2:c.946-2A>G', '-', 'r.spl?', 'p.(?)', 'CAPN3_00274', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['6i', 'NM_000070.2:c.946-1G>A', '-', 'r.945_946ins946-390_346-1{346-1g>a}', 'p.Thr316Glufs*2', 'CAPN3_00017', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/7720071,http://www.ncbi.nlm.nih.gov/pubmed/9655129', 'DNA, RNA', 'HD, RT-PCR, SEQ', '-', '-'], ['7', 'NM_000070.2:c.956C>T', '-', 'r.956c>u', 'p.Pro319Leu', 'CAPN3_00031', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09150160,http://www.omim.org/entry/114240#0005', 'DNA, RNA', 'RT-PCR, SEQ', '-', 'HphI+'], ['7', 'NM_000070.2:c.958G>T', '-', 'r.(?)', 'p.(Val320Phe)', 'CAPN3_00377', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['7', 'NM_000070.2:c.964T>C', '-', 'r.(?)', 'p.(Tyr322His)', 'CAPN3_00235', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['7', 'NM_000070.2:c.966T>A', '-', 'r.(?)', 'p.(Tyr322*)', 'CAPN3_00306', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['7', 'NM_000070.2:c.967G>T', '-', 'r.(?)', 'p.(Glu323*)', 'CAPN3_00236', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['7', 'NM_000070.2:c.984C>A', '-', 'r.(?)', 'p.(Cys328*)', 'CAPN3_00396', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16971480,http://www.ncbi.nlm.nih.gov/pubmed/17526799', 'DNA', 'SSCA', '-', '-'], ['7', 'NM_000070.2:c.984C>T', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00086', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['7', 'NM_000070.2:c.985G>A', '-', 'r.(?)', 'p.(Gly329Arg)', 'CAPN3_00275', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_000070.2:c.998G>A', '-', 'r.(?)', 'p.(Gly333Asp)', 'CAPN3_00394', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17318636', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_000070.2:c.1000C>T', '-', 'r.(?)', 'p.(His334Tyr)', 'CAPN3_00195', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['7', 'NM_000070.2:c.1001A>T', '-', 'r.(?)', 'p.(His334Leu)', 'CAPN3_00436', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['7', 'NM_000070.2:c.1001dupA', '-', 'r.(?)', 'p.(His334Glnfs*10)', 'CAPN3_00196', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['7', 'NM_000070.2:c.1002C>G', '-', 'r.(?)', 'p.(His334Gln)', 'CAPN3_00032', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09150160', 'DNA', 'SEQ', '-', 'AciI-'], ['7', 'NM_000070.2:c.1006T>A', '-', 'r.(?)', 'p.(Tyr336Asn)', 'CAPN3_00033', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09266733', 'DNA', 'SEQ', '-', '-'], ['7i', 'NM_000070.2:c.1029+1G>T', '-', 'r.spl?', 'p.?', 'CAPN3_00137', 'control chromosomes', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['7i', 'NM_000070.2:c.1029+3A>G', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00225', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['7i', 'NM_000070.2:c.1029+198C>T', '-', 'r.(=)', 'p.(=)', 'CAPN3_00340', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15689361', 'DNA', 'SEQ', '-', '-'], ['7i', 'NM_000070.2:c.1030-1G>A', '-', 'r.1030delG', 'p.V3al44Serfs*8', 'CAPN3_00454', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/20635405', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['8', 'NM_000070.2:c.1034C>T', '-', 'r.(?)', 'p.(Pro345Leu)', 'CAPN3_00180', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '2/330', '-'], ['8', 'NM_000070.2:c.1043delG', '-', 'r.(?)', 'p.(Gly348Valfs*4)', 'CAPN3_00199', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15733273', 'DNA', 'SEQ', '-', '-'], ['8', 'NM_000070.2:c.1058T>C', '-', 'r.(?)', 'p.(Leu353Pro)', 'CAPN3_00197', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['8', 'NM_000070.2:c.1061T>C', '-', 'r.(?)', 'p.(Val354Ala)', 'CAPN3_00198', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789,http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['8', 'NM_000070.2:c.1061T>G', '-', 'r.1061u>g', 'p.Val354Gly', 'CAPN3_00006', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789,http://www.ncbi.nlm.nih.gov/pubmed/20635405', 'DNA, RNA', 'DHPLC, RT-PCR, SEQ', '-', '-'], ['8', 'NM_000070.2:c.1063C>G', '-', 'r.(?)', 'p.(Arg355Gly)', 'CAPN3_00372', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['8', 'NM_000070.2:c.1063C>T', '-', 'r.(?)', 'p.(Arg355Trp)', 'CAPN3_00136', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['8', 'NM_000070.2:c.1069C>T', '-', 'r.(?)', 'p.(Arg357Trp)', 'CAPN3_00276', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['8', 'NM_000070.2:c.1070G>A', '-', 'r.(?)', 'p.(Arg357Gln)', 'CAPN3_00385', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15733273', 'DNA', 'SEQ', '-', 'ScaI+'], ['8', 'NM_000070.2:c.1076C>T', '-', 'r.(?)', 'p.(Pro359Leu)', 'CAPN3_00128', '-', 'germline (inherited)', '-', 'Ginjaar, Neuromuscul.Disord. 12:731,', 'DNA', 'DGGE', '-', '-'], ['8', 'NM_000070.2:c.1079G>A', '-', 'r.(?)', 'p.(Trp360*)', 'CAPN3_00007', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['8', 'NM_000070.2:c.1080G>C', '-', 'r.(?)', 'p.(Trp360Cys)', 'CAPN3_00035', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09771675,http://www.omim.org/entry/114240#0007', 'DNA', 'SEQ', '-', 'PstI-'], ['8', 'NM_000070.2:c.1099G>A', '-', 'r.(?)', 'p.(Gly367Ser)', 'CAPN3_00277', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['8', 'NM_000070.2:c.1106G>A', '-', 'r.(?)', 'p.(Trp369*)', 'CAPN3_00387', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15733273', 'DNA', 'SEQ', '-', '-'], ['8i', 'NM_000070.2:c.1115+5G>A', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00336', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['8i', 'NM_000070.2:c.1115+5G>T', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00156', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11525884', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['8i', 'NM_000070.2:c.1116-5A>G', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00503', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['8i', 'NM_000070.2:c.1116-1G>A', '-', 'r.[1116_1122del, 1116_1193del]', 'p.[Trp373Thrfs*59; Trp373_Trp398del]', 'CAPN3_00191', '-', 'germline (inherited)', '-', '-', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['9', 'NM_000070.2:c.1156C>T', '-', 'r.(?)', 'p.(Arg386Cys)', 'CAPN3_00278', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['9', 'NM_000070.2:c.1162C>T', '-', 'r.(?)', 'p.(Gln388*)', 'CAPN3_00510', '-', 'unknown', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['9', 'NM_000070.2:c.1191C>G', '-', 'r.(?)', 'p.(Phe397Leu)', 'CAPN3_00297', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['9', 'NM_000070.2:c.1192T>C', '-', 'r.(?)', 'p.(Trp398Arg)', 'CAPN3_00430', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['9', 'NM_000070.2:c.1193G>C', '-', 'r.(spl?)', 'p.(Trp398Ser?)', 'CAPN3_00179', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '-', '-'], ['9i', 'NM_000070.2:c.1193+6T>A', '-', 'r.(spl?)', 'p.?', 'CAPN3_00413', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['9i', 'NM_000070.2:c.1194-45C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00518', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['9i', 'NM_000070.2:c.1194-26C>G', '-', 'r.(?)', 'p.(=)', 'CAPN3_00087', 'determined on >100 chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ, SSCA', '0.07', 'AflIII'], ['9i', 'NM_000070.2:c.1194-9A>G', '-', 'r.(1148_1149ins1149-8_1149-1)?', 'p.fs?', 'CAPN3_00088', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['10', 'NM_000070.2:c.1202A>G', '-', 'r.(?)', 'p.(Tyr401Cys)', 'CAPN3_00298', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['10', 'NM_000070.2:c.1227A>G', '-', 'r.(?)', 'p.(=)', 'CAPN3_00519', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1250C>T', '-', 'r.(?)', 'p.(Thr417Met)', 'CAPN3_00279', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1256A>G', '-', 'r.(?)', 'p.(Asp419Gly)', 'CAPN3_00435', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1257T>G', '-', 'r.(?)', 'p.(Asp419Glu)', 'CAPN3_00280', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1259C>A', '-', 'r.(?)', 'p.(Ala420Asp)', 'CAPN3_00299', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['10', 'NM_000070.2:c.1263G>A', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00089', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', 'SfanI'], ['10', 'NM_000070.2:c.1286G>A', '-', 'r.(?)', 'p.(Trp429*)', 'CAPN3_00281', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1290A>G', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00249', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['10', 'NM_000070.2:c.1291G>A', '-', 'r.(?)', 'p.(Val431Met)', 'CAPN3_00115', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['10', 'NM_000070.2:c.1292dupT', '-', 'r.(?)', 'p.(Ser432Valfs*39)', 'CAPN3_00090', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-TthIII'], ['10', 'NM_000070.2:c.1298_1299del', '-', 'r.(?)', 'p.(Val434Glufs*37)', 'CAPN3_00388', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15733273', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1301A>T', '-', 'r.(?)', 'p.(Asn434Ile)', 'CAPN3_00376', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['10', 'NM_000070.2:c.1302C>T', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00357', '-', 'germline (inherited)', '-', 'Sacara ESHG2007, P676', 'DNA', 'SSCA, SEQ', '-', '-'], ['10', 'NM_000070.2:c.1303G>A', '-', 'r.(?)', 'p.(Glu435Lys)', 'CAPN3_00134', '-', 'germline (inherited)', '-', 'Politano et al., Neuromuscul.Disord. 12: 733', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1309C>G', '-', 'r.(?)', 'p.(Arg437Gly)', 'CAPN3_00414', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1309C>T', '-', 'r.(?)', 'p.(Arg437Cys)', 'CAPN3_00091', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['10', 'NM_000070.2:c.1312T>C', '-', 'r.(?)', 'p.(Trp438Arg)', 'CAPN3_00410', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1318C>T', '-', 'r.1318c>u', 'p.Arg440Trp', 'CAPN3_00036', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11525884', 'DNA, RNA', 'RT-PCR, SEQ', '-', 'SfanI'], ['10', 'NM_000070.2:c.1319G>A', '-', 'r.(?)', 'p.(Arg440Gln)', 'CAPN3_00161', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['10', 'NM_000070.2:c.1319_1322del', '-', 'r.(?)', 'p.(Arg440Leufs*22)', 'CAPN3_00092', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1322delG', '-', 'r.(?)', 'p.(Gly441Valfs*22)', 'CAPN3_00157', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1322G>A', '-', 'r.1322g>a', 'p.Gly441Asp', 'CAPN3_00093', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16372320', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['10', 'NM_000070.2:c.1327T>C?', '-', 'r.1327u>c', 'p.Ser443Pro', 'CAPN3_00349', '-', 'germline (inherited)', '-', '-', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['10', 'NM_000070.2:c.1328C>T', '-', 'r.(?)', 'p.(Ser443Phe)', 'CAPN3_00351', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', 'MspI'], ['10', 'NM_000070.2:c.1333G>A', '-', 'r.(?)', 'p.(Gly445Arg)', 'CAPN3_00094', '-', 'germline (inherited)', '-', 'Ginjaar WMS2005', 'DNA', 'DGGE', '-', '-'], ['10', 'NM_000070.2:c.1333G>C', '-', 'r.(?)', 'p.(Gly445Arg)', 'CAPN3_00511', '-', 'unknown', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['10', 'NM_000070.2:c.1336G>A', '-', 'r.(?)', 'p.(Gly446Ser)', 'CAPN3_00355', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1339T>C', '-', 'r.(?)', 'p.(Cys447Arg)', 'CAPN3_00282', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1342C>G', '-', 'r.(?)', 'p.(Arg448Gly)', 'CAPN3_00008', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1342C>T', '-', 'r.(?)', 'p.(Arg448Cys)', 'CAPN3_00095', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['10', 'NM_000070.2:c.1343G>A', '-', 'r.(?)', 'p.(Arg448His)', 'CAPN3_00096', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['10', 'NM_000070.2:c.1345A>C', '-', 'r.(?)', 'p.(Asn449His)', 'CAPN3_00158', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['10', 'NM_000070.2:c.1354G>C', '-', 'r.1354g>c', 'p.Asp452His', 'CAPN3_00153', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11525884', 'DNA, RNA', 'RT-PCR, SEQ', '-', 'ScaI+'], ['10i', 'NM_000070.2:c.1355-6G>A', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00434', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['10i', 'NM_000070.2:c.1355-6G>C', '-', 'r.(=)', 'p.(=)', 'CAPN3_00341', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15689361', 'DNA', 'SSCA', '-', '-'], ['10i', 'NM_000070.2:c.1355-1G>C', '-', 'r.spl?', 'p.(?)', 'CAPN3_00283', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['11', 'NM_000070.2:c.1355ins?', '-', 'r.1355ins?', 'p.fs', 'CAPN3_00116', '-', 'germline (inherited)', '-', '{DB: Hoffman}', 'DNA, RNA', 'SEQ', '-', '-'], ['11', 'NM_000070.2:c.1361T>C', '-', 'r.(?)', 'p.(Phe454Ser)', 'CAPN3_00301', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['11', 'NM_000070.2:c.1373delC', '-', 'r.1373del', 'p.Pro458Leufs*5', 'CAPN3_00097', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17979987', 'DNA, RNA', 'RT-PCR, DHPLC, SEQ', '-', '-'], ['11', 'NM_000070.2:c.1381C>T', '-', 'r.1381c>u', 'p.Arg461Cys', 'CAPN3_00141', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10567047', 'DNA, RNA', 'RT-PCR, SEQ', '-', 'ScaI+'], ['11', 'NM_000070.2:c.1385T>G', '-', 'r.(?)', 'p.(Leu462Arg)', 'CAPN3_00261', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '-', '-'], ['11', 'NM_000070.2:c.1401_1403del', '-', 'r.(?)', 'p.(Glu467del)', 'CAPN3_00200', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['11', 'NM_000070.2:c.1435A>G', '-', 'r.(?)', 'p.(Ser479Gly)', 'CAPN3_00098', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['11', 'NM_000070.2:c.1448C>A', '-', 'r.(?)', 'p.(Ala483Asp)', 'CAPN3_00202', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['11', 'NM_000070.2:c.1450C>A', '-', 'r.(?)', 'p.(Leu484Met)', 'CAPN3_00302', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['11', 'NM_000070.2:c.1456C>G', '-', 'r.(?)', 'p.(Gln486Glu)', 'CAPN3_00037', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/9762961', 'DNA', 'SEQ', '-', '-SfaNI'], ['11', 'NM_000070.2:c.1465C>T', '-', 'r.(?)', 'p.(Arg489Trp)', 'CAPN3_00038', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/9762961', 'DNA', 'SEQ', '-', 'Cfr10I-;BsrI+'], ['11', 'NM_000070.2:c.1466G>A', '-', 'r.(?)', 'p.(Arg489Gln)', 'CAPN3_00018', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', 'DdeI-'], ['11', 'NM_000070.2:c.1468C>T', '-', 'r.(?)', 'p.(Arg490Trp)', 'CAPN3_00009', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789,http://www.ncbi.nlm.nih.gov/pubmed/14578192,http://www.ncbi.nlm.nih.gov/pubmed/15725583', 'DNA', 'DHPLC', '-', '-'], ['11', 'NM_000070.2:c.1469G>A', '-', 'r.1469g>a', 'p.Arg490Gln', 'CAPN3_00034', '-', 'germline (inherited)', '-', '{DB: Hoffman}', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['11', 'NM_000070.2:c.1477C>G', '-', 'r.(?)', 'p.(Arg493Gly)', 'CAPN3_00204', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['11', 'NM_000070.2:c.1477C>T', '-', 'r.(?)', 'p.(Arg493Trp)', 'CAPN3_00070', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', 'Cfr10I-'], ['11', 'NM_000070.2:c.1486G>A', '-', 'r.(?)', 'p.(Gly496Arg)', 'CAPN3_00039', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', 'MboI-'], ['11', 'NM_000070.2:c.1505T>C', '-', 'r.(?)', 'p.(Ile502Thr)', 'CAPN3_00391', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA, DGGE', '-', '-'], ['11', 'NM_000070.2:c.1524G>A', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00132', '-', 'germline (inherited)', '-', 'Meznaric-Petrusa, Neuromuscul.Disord. 12: 731', 'DNA', 'DHPLC', '-', '-'], ['11i', 'NM_000070.2:c.1524+1G>C', '-', 'r.spl?', 'p.?', 'CAPN3_00284', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['11i', 'NM_000070.2:c.1524+6C>T', '-', 'r.(?)', 'p.(?)', 'CAPN3_00099', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/9452114', 'DNA', 'SEQ', '-', '-'], ['11i', 'NM_000070.2:c.1524+47G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00358', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['11i', 'NM_000070.2:c.1524+81C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00250', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['11i', 'NM_000070.2:c.1524+129C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00359', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['12i', 'NM_000070.2:c.1536+1G>T', '-', 'r.1536_1537ins1536+1_1537-1{1536+1G>T}', 'p.Met513Ilefs*2', 'CAPN3_00407', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/20477750', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['12i', 'NM_000070.2:c.1536+133T>C', '-', 'r.(=)', 'p.(=)', 'CAPN3_00343', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15689361', 'DNA', 'SSCA, SEQ', '-', '-'], ['12i', 'NM_000070.2:c.1537-48T>C', '-', 'r.spl?', 'p.(?)', 'CAPN3_00258', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['12i', 'NM_000070.2:c.1537-40C>G', '-', 'r.spl?', 'p.(?)', 'CAPN3_00378', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['12i', 'NM_000070.2:c.1537-33G>A', '-', 'r.(=)', 'p.(=)', 'CAPN3_00342', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15689361', 'DNA', 'SSCA, SEQ', '-', '-'], ['12i', 'NM_000070.2:c.1537-1G>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00304', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['13', 'NM_000070.2:c.1542C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00251', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['13', 'NM_000070.2:c.1566G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00356', '-', 'germline (inherited)', '-', 'Ginjaar, Neuromuscul.Disord. 12:731,', 'DNA', 'DGGE, SEQ', '-', '-'], ['13', 'NM_000070.2:c.1567G>A', '-', 'r.1567g>a', 'p.Asp523Asn', 'CAPN3_00117', '-', 'germline (inherited)', '-', '{DB: Hoffman}', 'DNA, RNA', 'SEQ', '-', '-'], ['13', 'NM_000070.2:c.1573_1575del', '1573_1575delTTC', 'r.(?)', 'p.(Phe525del)', 'CAPN3_00149', '-', 'germline (inherited)', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['13', 'NM_000070.2:c.1574T>C', '-', 'r.(?)', 'p.(Phe525Ser)', 'CAPN3_00285', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['13', 'NM_000070.2:c.1610A>G', '-', 'r.(?)', 'p.(Tyr537Cys)', 'CAPN3_00305', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['13', 'NM_000070.2:c.1611C>A', '-', 'r.(?)', 'p.(Tyr537*)', 'CAPN3_00041', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-'], ['13', 'NM_000070.2:c.1621C>T', '-', 'r.(?)', 'p.(Arg541Trp)', 'CAPN3_00129', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['13', 'NM_000070.2:c.1622G>A', '-', 'r.(?)', 'p.(Arg541Gln)', 'CAPN3_00024', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-'], ['13', 'NM_000070.2:c.1641C>A', '-', 'r.(?)', 'p.(Phe547Leu)', 'CAPN3_00232', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['13', 'NM_000070.2:c.1657G>A', '-', 'r.(?)', 'p.(Glu553Lys)', 'CAPN3_00138', 'control chromosomes', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['13', 'NM_000070.2:c.1662C>G', '1654C>G', 'r.(?)', 'p.(Tyr554*)', 'CAPN3_00415', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['13', 'NM_000070.2:c.1663G>A', '-', 'r.(?)', 'p.(Val555Ile)', 'CAPN3_00286', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['13', 'NM_000070.2:c.1667T>C', '-', 'r.(?)', 'p.(Ile556Thr)', 'CAPN3_00307', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['13', 'NM_000070.2:c.1668C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00101', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ, SSCA', '<0.01', '-'], ['13', 'NM_000070.2:c.1693delC', '-', 'r.(?)', 'p.(Gln565Argfs*30)', 'CAPN3_00389', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15733273', 'DNA', 'SEQ', '-', 'HhaI-;HgiaI+'], ['13', 'NM_000070.2:c.1694A>C', '-', 'r.1694a>c', 'p.Gln565Pro', 'CAPN3_00404', '-', 'germline (inherited)', '-', '-', 'DNA, RNA', 'SEQ', '-', '-'], ['13', 'NM_000070.2:c.1699G>T', '-', 'r.(?)', 'p.(Gly567Trp)', 'CAPN3_00042', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['13', 'NM_000070.2:c.1706T>C', '-', 'r.(?)', 'p.(Phe569Ser)', 'CAPN3_00205', '-', 'germline (inherited)', '-', '{DBSubm098}', 'DNA', 'SEQ', '-', '-'], ['13', 'NM_000070.2:c.1711delC', '-', 'r.(?)', 'p.(Leu571Serfs*24)', 'CAPN3_00416', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['13', 'NM_000070.2:c.1714C>T', '-', 'r.(?)', 'p.(Arg572Trp)', 'CAPN3_00043', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['13', 'NM_000070.2:c.1715G>A', '-', 'r.(?)', 'p.(Arg572Gln)', 'CAPN3_00011', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', 'NciI-'], ['13', 'NM_000070.2:c.1715G>C', '-', 'r.(?)', 'p.(Arg572Pro)', 'CAPN3_00206', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['13', 'NM_000070.2:c.1722delC', '-', 'r.1722delC', 'p.Ser575Leufs*20', 'CAPN3_00168', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15351423,http://www.ncbi.nlm.nih.gov/pubmed/16372320', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['13', 'NM_000070.2:c.1742C>G', '-', 'r.1742c>g', 'p.Ser581Cys', 'CAPN3_00155', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11525884', 'DNA, RNA', 'RT-PCR, SEQ', '-', 'DdeI-;SecI+'], ['13', 'NM_000070.2:c.1743_1744del', '-', 'r.(?)', 'p.(Glu582Glyfs*3)', 'CAPN3_00102', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-'], ['13i', 'NM_000070.2:c.1745+1G>A', '-', 'r.spl?', 'p.?', 'CAPN3_00207', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['13i', 'NM_000070.2:c.1745+4_1745+7del', '-', 'r.1659_1745del', 'p.Tyr554_Glu582del', 'CAPN3_00411', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17979987', 'DNA, RNA', 'RT-PCR, DHPLC, SEQ', '-', '-'], ['13i', 'NM_000070.2:c.1745+5G>A', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00335', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['13i', 'NM_000070.2:c.1745+5G>C', '-', 'r.spl?', 'p.(?)', 'CAPN3_00121', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['13i', 'NM_000070.2:c.1746-64C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00257', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?type=rs&rs=rs17764849', 'DNA', 'DHPLC, SEQ', '0.02', '-'], ['13i', 'NM_000070.2:c.1746-20C>G', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00140', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['14', 'NM_000070.2:c.1763T>C', '-', 'r.(?)', 'p.(Ile588Thr)', 'CAPN3_00525', '-', 'germline (inherited)', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['14i', 'NM_000070.2:c.1782+23_1782+24insAGAG', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00252', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?type=rs&rs=rs10697562', 'DNA', 'SEQ', '-', '-'], ['14i', 'NM_000070.2:c.1782+1072G>C', '-', 'r.1782_1783ins1783-1070_1783-971', 'p.Lys595Valfs*70', 'CAPN3_00405', '-', 'germline (inherited)', '-', '-', 'DNA, RNA', 'SEQ', '-', '-'], ['14i', 'NM_000070.2:c.1783-63C>G', '-', 'r.(=)', 'p.(=)', 'CAPN3_00344', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15689361', 'DNA', 'SSCA, SEQ', '-', '-'], ['14i', 'NM_000070.2:c.1783-59C>T', '-', 'r.(=)', 'p.(=)', 'CAPN3_00345', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15689361', 'DNA', 'SSCA, SEQ', '-', '-'], ['14i', 'NM_000070.2:c.1783-5_1784del', '-', 'r.spl?', 'p.(?)', 'CAPN3_00287', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['14i', 'NM_000070.2:c.1783-?insCTCT', 'IVS14insCTCT', 'r.(=)', 'p.(=)', 'CAPN3_00000', '-', 'germline (inherited)', '-', 'La Russa ESHG2008 P01.205', 'DNA', 'SEQ', '-', '-'], ['15', 'NM_000070.2:c.1788_1791del', '-', 'r.(?)', 'p.(Lys598Profs*63)', 'CAPN3_00048', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-'], ['15', 'NM_000070.2:c.1788_1793del', '1783_1788del', 'r.1788_1793del', 'p.Lys597_Lys598del', 'CAPN3_00169', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15351423,http://www.ncbi.nlm.nih.gov/pubmed/16372320', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['15', 'NM_000070.2:c.1792_1795del', '-', 'r.(?)', 'p.(Lys598Profs*63)', 'CAPN3_00163', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['15', 'NM_000070.2:c.1795dupA', '-', 'r.1795dup', 'p.Thr559Asnfs*33', 'CAPN3_00045', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11525884', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['15i', 'NM_000070.2:c.1800+2T>C', '-', 'r.spl?', 'p.(?)', 'CAPN3_00308', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['15i', 'NM_000070.2:c.1800+21C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00360', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['15i', 'NM_000070.2:c.1801-51G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00181', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '2/76', '-'], ['16', 'NM_000070.2:c.1811_1812del', '-', 'r.(?)', 'p.(Phe604Cysfs*27)', 'CAPN3_00395', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17318636', 'DNA', 'SEQ', '-', '-'], ['16', 'NM_000070.2:c.1813G>A', '-', 'r.(?)', 'p.(Val605Ile)', 'CAPN3_00520', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['16', 'NM_000070.2:c.1817C>T', '-', 'r.1817c>u', 'p.Ser606Leu', 'CAPN3_00040', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/09150160', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['16', 'NM_000070.2:c.1823G>A', '-', 'r.(?)', 'p.(Arg608Lys)', 'CAPN3_00417', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['16', 'NM_000070.2:c.1826C>A', '-', 'r.(?)', 'p.(Ala609Glu)', 'CAPN3_00346', 'control chromosomes', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['16', 'NM_000070.2:c.1838delA', '-', 'r.(?)', 'p.(Lys613Argfs*49)', 'CAPN3_00004', 'reported to database by Richard', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'HD, SEQ', '-', 'AvaI+'], ['16', 'NM_000070.2:c.1855C>T', '-', 'r.(?)', 'p.(Gln619*)', 'CAPN3_00453', '-', 'germline (inherited)', '-', 'Stehlikova ESHG2009 P16.45', 'DNA', 'SEQ', '-', '-'], ['16', 'NM_000070.2:c.1858del', '-', 'r.(?)', 'p.(Glu620Serfs*42)', 'CAPN3_00512', '-', 'unknown', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['16', 'NM_000070.2:c.1865A>C', '-', 'r.(?)', 'p.(Glu622Ala)', 'CAPN3_00237', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?type=rs&rs=rs11557723', 'DNA', 'SEQ', '-', '-'], ['16', 'NM_000070.2:c.1865_1866del', '-', 'r.(?)', 'p.(Glu622Glyfs*9)', 'CAPN3_00103', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['16', 'NM_000070.2:c.1868_1877del', '1868_1877del', 'r.(?)', 'p.(Glu623Alafs*36)', 'CAPN3_00208', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['16', 'NM_000070.2:c.1872C>T', '-', 'r.1871_1914del', 'p.Gly624Alafs*7', 'CAPN3_00046', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/7670461', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['16', 'NM_000070.2:c.1897C>T', '-', 'r.(?)', 'p.(Gln633*)', 'CAPN3_00433', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['16', 'NM_000070.2:c.1910delC', '-', 'r.(?)', 'p.(Pro637Hisfs*25)', 'CAPN3_00309', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['16', 'NM_000070.2:c.1913A>C', '-', 'r.(?)', 'p.(Gln638Pro)', 'CAPN3_00023', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA, DGGE', '-', '-'], ['16i', 'NM_000070.2:c.1914+30G>A', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00253', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['17', 'NM_000070.2:c.1917_1922del', '-', 'r.(?)', 'p.(Gln640_Pro641del)', 'CAPN3_00209', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['17', 'NM_000070.2:c.1939G>T', '-', 'r.(?)', 'p.(Glu647*)', 'CAPN3_00418', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['17', 'NM_000070.2:c.1968_1981dup', '1967_1980dup', 'r.(?)', 'p.(Ile661Thrfs*6)', 'CAPN3_00419', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/19835634', 'DNA', 'SEQ', '-', '-'], ['17', 'NM_000070.2:c.1971_1973del', '-', 'r.(?)', 'p.(Phe658del)', 'CAPN3_00398', '-', 'germline (inherited)', '-', '{DBSubm098}', 'DNA', 'SEQ', '-', '-'], ['17', 'NM_000070.2:c.1979A>G', '-', 'r.(?)', 'p.(Gln660Arg)', 'CAPN3_00310', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['17', 'NM_000070.2:c.1981delA', '-', 'r.(?)', 'p.(Ile661*)', 'CAPN3_00104', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['17', 'NM_000070.2:c.1981_1984del', '-', 'r.(?)', 'p.(Ile661Glnfs*20)', 'CAPN3_00062', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', 'BsrI+'], ['17', 'NM_000070.2:c.1983delA', '-', 'r.(?)', 'p.(Ile661Metfs*21)', 'CAPN3_00105', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340,http://www.ncbi.nlm.nih.gov/pubmed/11297944,http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SSCA, SEQ', '-', '-'], ['17', 'NM_000070.2:c.1984G>T', '-', 'r.(?)', 'p.(Ala662Ser)', 'CAPN3_00210', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['17i', 'NM_000070.2:c.1992+1G>T', '-', 'r.spl?', 'p.(?)', 'CAPN3_00106', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['17i', 'NM_000070.2:c.1992+42C>G', '-', 'r.(?)', 'p.(=)', 'CAPN3_00521', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['17i', 'NM_000070.2:c.1992+100C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00361', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['17i', 'NM_000070.2:c.1993-5_1993-3delCTC', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00254', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['17i', 'NM_000070.2:c.1993-1G>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00288', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['17i', 'NM_000070.2:c.1993-1G>T', '-', 'r.spl?', 'p.(?)', 'CAPN3_00072', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340,http://www.ncbi.nlm.nih.gov/pubmed/11297944,http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SSCA, SEQ', '-', '-'], ['18', 'NM_000070.2:c.1999dupG', '-', 'r.1999dupg', 'p.Glu677Glyfs*6', 'CAPN3_00152', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11525884', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['18', 'NM_000070.2:c.2005T>A', '-', 'r.(?)', 'p.(Cys669Ser)', 'CAPN3_00289', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['18', 'NM_000070.2:c.2019C>G', '-', 'r.(?)', 'p.(=)', 'CAPN3_00107', 'determined on >100 chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ, SSCA', '<0.01', '-'], ['18', 'NM_000070.2:c.2023_2025del', '-', 'r.(?)', 'p.(Lys675del)', 'CAPN3_00211', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['18', 'NM_000070.2:c.2036_2037del', '-', 'r.(?)', 'p.(Thr679Serfs*20)', 'CAPN3_00290', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['18i', 'NM_000070.2:c.2050+1delG', '-', 'r.spl?', 'p.(?)', 'CAPN3_00311', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['18i', 'NM_000070.2:c.2050+1G>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00154', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11525884', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['18i', 'NM_000070.2:c.2050+29G>A', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00432', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['18i', 'NM_000070.2:c.2050+36G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00362', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['19', 'NM_000070.2:c.2069_2070del', '-', 'r.(?)', 'p.(His690Argfs*9)', 'CAPN3_00012', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['19', 'NM_000070.2:c.2071G>A', '-', 'r.(?)', 'p.(Gly691Arg)', 'CAPN3_00522', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['19', 'NM_000070.2:c.2071_2080del', '-', 'r.2071_2080del', 'p.Gly691Trpfs*7', 'CAPN3_00406', '-', 'germline (inherited)', '-', '-', 'DNA, RNA', 'SEQ', '-', '-'], ['19', 'NM_000070.2:c.2077A>C', '-', 'r.(?)', 'p.(Thr693Pro)', 'CAPN3_00313', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['19', 'NM_000070.2:c.2092C>A', '-', 'r.(?)', 'p.(Arg698Ser)', 'CAPN3_00452', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['19', 'NM_000070.2:c.2092C>T', '-', 'r.(?)', 'p.(Arg698Cys)', 'CAPN3_00291', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['19', 'NM_000070.2:c.2093G>C', '-', 'r.(?)', 'p.(Arg698Pro)', 'CAPN3_00077', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340,http://www.ncbi.nlm.nih.gov/pubmed/11297944,http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SSCA, SEQ', '-', '-'], ['19', 'NM_000070.2:c.2105C>A', 'c.2105C>T', 'r.(?)', 'p.(Ala702Glu)', 'CAPN3_00441', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['19', 'NM_000070.2:c.2105C>T', '-', 'r.(?)', 'p.(Ala702Val)', 'CAPN3_00047', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['19', 'NM_000070.2:c.2113G>C', '-', 'r.(?)', 'p.(Asp705His)', 'CAPN3_00108', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['19', 'NM_000070.2:c.2114A>G', '-', 'r.(spl?)', 'p.(Asp705Gly)', 'CAPN3_00109', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11297944', 'DNA', 'SSCA', '-', '-'], ['19i', 'NM_000070.2:c.2115+1_2115+2dup', '-', 'r.spl?', 'p.(?)', 'CAPN3_00127', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '-', '-'], ['19i', 'NM_000070.2:c.2115+4T>A', '-', 'r.(spl?)', 'p.?', 'CAPN3_00363', 'effect on splicing uncertain', 'germline (inherited)', '-', 'Ginjaar, WMS2008', 'DNA', 'DGGE, SEQ', '-', '-'], ['19i', 'NM_000070.2:c.2115+46G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00255', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['20', 'NM_000070.2:c.2117C>A', '-', 'r.(?)', 'p.(Thr706Lys)', 'CAPN3_00162', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15733273', 'DNA', 'SEQ', '-', '-'], ['20', 'NM_000070.2:c.2120A>G', '-', 'r.2120a>g', 'p.Asp707Gly', 'CAPN3_00118', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10567047', 'DNA, RNA', 'RT-PCR, SEQ', '-', '-'], ['20', 'NM_000070.2:c.2134C>T', '-', 'r.(?)', 'p.(Leu712Phe)', 'CAPN3_00130', '-', 'germline (inherited)', '-', 'Ginjaar WMS2005', 'DNA', 'DGGE', '-', '-'], ['20', 'NM_000070.2:c.2148G>T', '-', 'r.(?)', 'p.(Glu716Asp)', 'CAPN3_00296', '-', 'germline (inherited)', '-', '-', 'DNA', 'DGGE, SEQ', '-', '-'], ['20', 'NM_000070.2:c.2177_2184+8del', '-', 'r.spl?', 'p.(?)', 'CAPN3_00292', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['20', 'NM_000070.2:c.2182C>T', '-', 'r.(?)', 'p.(Gln728*)', 'CAPN3_00133', '-', 'germline (inherited)', '-', 'Ginjaar WMS2005', 'DNA', 'DGGE', '-', '-'], ['20', 'NM_000070.2:c.2184G>A', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00212', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['20i', 'NM_000070.2:c.2184+3G>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00334', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['20i', 'NM_000070.2:c.2185-16A>G', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00300', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['20i', 'NM_000070.2:c.2185-12_2194del', '-', 'r.spl?', 'p.(?)', 'CAPN3_00079', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['20i', 'NM_000070.2:c.2185-2A>G', '-', 'r.spl?', 'p.(?)', 'CAPN3_00084', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['21', 'NM_000070.2:c.2190_2196del', '-', 'r.(?)', 'p.(Phe731Thrfs*43)', 'CAPN3_00374', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['21', 'NM_000070.2:c.2192T>C', '-', 'r.(?)', 'p.(Phe731Ser)', 'CAPN3_00081', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-XmnI'], ['21', 'NM_000070.2:c.2207_2208del', '-', 'r.(?)', 'p.(Thr736Argfs*28)', 'CAPN3_00213', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['21', 'NM_000070.2:c.2212C>T', '-', 'r.(?)', 'p.(Gln738*)', 'CAPN3_00214', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['21', 'NM_000070.2:c.2226_2240del', '-', 'r.2226_2240del', 'p.Ile742_Glu746del', 'CAPN3_00442', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17897828', 'DNA, RNA', 'RT-PCR, SEQ', '?', '?'], ['21', 'NM_000070.2:c.2227_2230dup', '-', 'r.(?)', 'p.(Ser744Lysfs*22)', 'CAPN3_00364', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789,http://www.ncbi.nlm.nih.gov/pubmed/15221789,http://www.ncbi.nlm.nih.gov/pubmed/15725583', 'DNA', 'DHPLC', '-', '-'], ['21', 'NM_000070.2:c.2230A>G', '-', 'r.(?)', 'p.(Ser744Gly)', 'CAPN3_00019', 'not in 120 control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/7720071,http://www.ncbi.nlm.nih.gov/pubmed/9655129', 'DNA', 'HD, SEQ', '-', 'AluI-'], ['21', 'NM_000070.2:c.2231G>C', '-', 'r.(?)', 'p.(Ser744Thr)', 'CAPN3_00397', '-', 'germline (inherited)', '-', '{DBSubm098}', 'DNA', 'SEQ', '-', '-'], ['21', 'NM_000070.2:c.2235C>G', '-', 'r.(?)', 'p.(Tyr745*)', 'CAPN3_00314', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['21', 'NM_000070.2:c.2235C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00365', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['21', 'NM_000070.2:c.2242C>T', '-', 'r.(?)', 'p.(Arg748*)', 'CAPN3_00123', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['21', 'NM_000070.2:c.2243G>A', '-', 'r.(?)', 'p.(Arg748Gln)', 'CAPN3_00028', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['21', 'NM_000070.2:c.2245A>C', '-', 'r.2245a>c', 'p.Asn749His', 'CAPN3_00337', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16372320,http://www.ncbi.nlm.nih.gov/pubmed/17157502', 'DNA, RNA', 'RT-PCR, SEQ, DHPLC', '-', '-'], ['21', 'NM_000070.2:c.2251_2254dup', '2251_2254dupGTCA', 'r.(?)', 'p.(Asn752Serfs*14)', 'CAPN3_00527', '-', 'germline (inherited)', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['21', 'NM_000070.2:c.2257delinsAA', '-', 'r.(?)', 'p.(Asp753Lysfs*12)', 'CAPN3_00215', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['21', 'NM_000070.2:c.2257G>A', '-', 'r.(?)', 'p.(Asp753Asn)', 'CAPN3_00166', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789', 'DNA', 'DHPLC', '-', '-'], ['21i', 'NM_000070.2:c.2263+1G>C', '-', 'r.spl?', 'p.(?)', 'CAPN3_00293', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['21i', 'NM_000070.2:c.2263+2T>A', '-', 'r.spl?', 'p.(?)', 'CAPN3_00110', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SEQ', '-', '-'], ['21i', 'NM_000070.2:c.2264-1G>C', '-', 'r.(?)', 'p.(?)', 'CAPN3_00384', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['22', 'NM_000070.2:c.2269C>G', '-', 'r.(?)', 'p.(His757Asp)', 'CAPN3_00131', '-', 'germline (inherited)', '-', 'Ginjaar, Neuromuscul.Disord. 12:731,', 'DNA', 'DGGE', '-', '-'], ['22', 'NM_000070.2:c.2279dupA', '-', 'r.(?)', 'p.(Asn760Lysfs*5)', 'CAPN3_00399', '-', 'germline (inherited)', '-', '{DBSubm098}', 'DNA', 'SEQ', '-', '-'], ['22', 'NM_000070.2:c.2288A>G', '-', 'r.2288a>g', 'p.Tyr763Cys', 'CAPN3_00119', '-', 'germline (inherited)', '-', '{DB: Hoffman}', 'DNA, RNA', 'SEQ', '-', '-'], ['22', 'NM_000070.2:c.2290del', '-', 'r.(?)', 'p.(Asp764Thrfs*12)', 'CAPN3_00455', '-', 'germline (inherited)', '-', '-', 'DNA', 'PCR, SEQ', '-', '-'], ['22', 'NM_000070.2:c.2292C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00256', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['22', 'NM_000070.2:c.2295_2297del', '-', 'r.(?)', 'p.(Ile765del)', 'CAPN3_00148', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/12461690', 'DNA', 'SSCA, DHPLC', '-', '-'], ['22', 'NM_000070.2:c.2306G>A', '-', 'r.(?)', 'p.(Arg769Gln)', 'CAPN3_00013', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['22', 'NM_000070.2:c.2306G>C', '-', 'r.(?)', 'p.(Arg769Pro)', 'CAPN3_00369', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11785010,http://www.ncbi.nlm.nih.gov/pubmed/16607617', 'DNA', 'DHPLC', '-', '-'], ['22', 'NM_000070.2:c.2314_2317del', '-', 'r.(?)', 'p.(Asp772Asnfs*3)', 'CAPN3_00014', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['22', 'NM_000070.2:c.2317_2321delinsT', '-', 'r.(?)', 'p.(Lys773Serfs*2)', 'CAPN3_00085', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-TthII, +BspHI'], ['22', 'NM_000070.2:c.2318_2321dup', '-', 'r.(?)', 'p.(His774Glnfs*8)', 'CAPN3_00315', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['22', 'NM_000070.2:c.2319dupA', '-', 'r.(?)', 'p.(His774Thrfs*7)', 'CAPN3_00111', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA, DGGE', '-', '-'], ['22', 'NM_000070.2:c.2320C>G', 'H774D', 'r.(?)', 'p.(His774Asp)', 'CAPN3_00112', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/11053681,http://www.ncbi.nlm.nih.gov/pubmed/10330340', 'DNA', 'SSCA', '-', '-'], ['22', 'NM_000070.2:c.2330T>C', '-', 'r.(?)', 'p.(Ile777Thr)', 'CAPN3_00216', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15221789,http://www.ncbi.nlm.nih.gov/pubmed/15725583,http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['22', 'NM_000070.2:c.2332G>A', '-', 'r.(?)', 'p.(Asp778Asn)', 'CAPN3_00366', '-', 'germline (inherited)', '-', '-', 'DNA', 'DGGE, SEQ', '-', '-'], ['22', 'NM_000070.2:c.2335T>A', '-', 'r.(?)', 'p.(Phe779Ile)', 'CAPN3_00217', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['22', 'NM_000070.2:c.2338G>C', '-', 'r.(?)', 'p.(Asp780His)', 'CAPN3_00159', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/15733273', 'DNA', 'SEQ', '-', '-'], ['22', 'NM_000070.2:c.2362_2363delinsTCATCT', '-', 'r.(?)', 'p.(Arg788Serfs*14)', 'CAPN3_00015', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['22', 'NM_000070.2:c.2371G>A', '-', 'r.(?)', 'p.(Glu791Ser)', 'CAPN3_00316', '-', 'germline (inherited)', '-', '-', 'DNA', 'SSCA', '-', '-'], ['22', 'NM_000070.2:c.2371G>T', '-', 'r.(?)', 'p.(Gly791Cys)', 'CAPN3_00424', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['22', 'NM_000070.2:c.2376G>A', '-', 'r.(?)', 'p.(Met792Ile)', 'CAPN3_00425', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['22i', 'NM_000070.2:c.2380+1G>T', '-', 'r.[2264_2380del, 2307_2380del]', 'p.[Phe756_Arg794del, Tyr770Serfs*6]', 'CAPN3_00426', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['22i', 'NM_000070.2:c.2380+2T>G', '-', 'r.spl?', 'p.(?)', 'CAPN3_00151', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/18055493', 'DNA', 'SEQ', '-', '-'], ['22i', 'NM_000070.2:c.2380+12A>G', '-', 'r.(?)', 'p.(=)', 'CAPN3_00523', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['22i', 'NM_000070.2:c.2380+12delA', '-', 'r.spl?', 'p.(?)', 'CAPN3_00113', 'pathogenicity unclear', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['22i', 'NM_000070.2:c.2380+19C>T', '-', 'r.(spl?)', 'p.(?)', 'CAPN3_00350', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['22i', 'NM_000070.2:c.2380+20dupT', '-', 'r.(?)', 'p.(=)', 'CAPN3_00352', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['22i', 'NM_000070.2:c.2381-129G>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00182', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '1/76', '-'], ['22i', 'NM_000070.2:c.2381-79T>C', '-', 'r.(?)', 'p.(=)', 'CAPN3_00183', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC, SEQ', '2/76', '-'], ['22i', 'NM_000070.2:c.2381-12A>G', '-', 'r.(?)', 'p.(=)', 'CAPN3_00367', '-', 'germline (inherited)', '-', '-', 'DNA', 'DGGE, SEQ', '-', '-'], ['23', 'NM_000070.2:c.2390A>C', '2380A>C', 'r.(?)', 'p.(His797Pro)', 'CAPN3_00427', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['23', 'NM_000070.2:c.2393C>A', '-', 'r.(?)', 'p.(Ala798Glu)', 'CAPN3_00114', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['23', 'NM_000070.2:c.2420T>C', '-', 'r.(?)', 'p.(Ile807Thr)', 'CAPN3_00381', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16650086', 'DNA', 'DHPLC', '-', '-'], ['23', 'NM_000070.2:c.2433T>C', '-', 'r.(?)', 'p.(=)', 'CAPN3_00504', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['23', 'NM_000070.2:c.2435T>C', '-', 'r.(?)', 'p.(Leu812Pro)', 'CAPN3_00509', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['23i', 'NM_000070.2:c.2439+69C>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00368', '-', 'germline (inherited)', '-', '-', 'DNA', 'DGGE, SEQ', '-', '-'], ['23i', 'NM_000070.2:c.2440-46G>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00524', 'http://genetics.emory.edu/egl/emvclass/emvclass.php', 'unknown', '-', '-', 'DNA', 'SEQ', '-', '-'], ['23i', 'NM_000070.2:c.2440-45delG', '-', 'r.(?)', 'p.(=)', 'CAPN3_00186', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '2/76', '-'], ['23i', 'NM_000070.2:c.2440-45dupG', '-', 'r.(?)', 'p.(=)', 'CAPN3_00185', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/entrez/viewer.fcgi?cmd=Retrieve&db=nucleotide&dopt=GenBank&list_uids=AF209502.1', 'DNA', 'DHPLC', '1/76', '-'], ['23i', 'NM_000070.2:c.2440-45_2440-42del', '2440-42_2440-45del', 'r.(?)', 'p.(=)', 'CAPN3_00187', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '2/76', '-'], ['23i', 'NM_000070.2:c.2440-45_2440-41del', '2440-41_2440-45del', 'r.(?)', 'p.(=)', 'CAPN3_00188', '-', 'germline (inherited)', '-', '-', 'DNA', 'DHPLC', '2/76', '-'], ['23i', 'NM_000070.2:c.2440-42A>T', '-', 'r.(?)', 'p.(=)', 'CAPN3_00505', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['23i', 'NM_000070.2:c.2440-6_2440-3del', '2440-7_2440-4del', 'r.spl?', 'p.(?)', 'CAPN3_00218', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/16141003', 'DNA', 'DHPLC', '-', '-'], ['23i', 'NM_000070.2:c.2440-3C>G', '-', 'r.spl?', 'p.(?)', 'CAPN3_00294', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['23i', 'NM_000070.2:c.2440-1G>C', '-', 'r.spl?', 'p.(?)', 'CAPN3_00449', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['24', 'NM_000070.2:c.2442G>A', '-', 'r.(?)', 'p.(Trp814*)', 'CAPN3_00431', 'control chromosomes', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/pubmed/17994539', 'DNA', 'SEQ', '-', '-'], ['24', 'NM_000070.2:c.2464T>C', '-', 'r.(?)', 'p.(*822Argext62*)', 'CAPN3_00125', '-', 'germline (inherited)', '-', 'Ginjaar, Neuromuscul.Disord. 12:731,', 'DNA', 'DGGE', '-', '-'], ['24', 'NM_000070.2:c.*51T>A', '-', 'r.(?)', 'p.(=)', 'CAPN3_00502', '-', 'germline (inherited)', '-', '-', 'DNA', 'SEQ', '-', '-'], ['24', 'NM_000070.2:c.*134C>T', '-', 'r.*134c>u', 'p.(=)', 'CAPN3_00189', '-', 'germline (inherited)', '-', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?type=rs&rs=rs3098423', 'DNA', 'DGGE, SEQ', '-', '-']]


#LOVD3 Test Pages
GEDI_HOMEPAGE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>View all genes - The Genetic Eye Disorder (GEDI) Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <META name="author" content="LOVD development team, LUMC, Netherlands">
  <META name="generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <BASE href="http://mseqdr.lumc.edu/GEDI/">
  <LINK rel="stylesheet" type="text/css" href="styles.css">
  <LINK rel="shortcut icon" href="favicon.ico" type="image/x-icon">

  <SCRIPT type="text/javascript" src="inc-js-openwindow.php"> </SCRIPT>
  <SCRIPT type="text/javascript" src="inc-js-toggle-visibility.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery.min.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery-ui.custom.min.js"> </SCRIPT>

  <SCRIPT type="text/javascript">
    <!--


    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jeegoocontext/jquery.jeegoocontext.min.js"> </SCRIPT>
  <LINK rel="stylesheet" type="text/css" href="lib/jeegoocontext/style.css">
  <LINK rel="stylesheet" type="text/css" href="lib/jQuery/css/cupertino/jquery-ui.custom.css">
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD valign="top" width="424" height="105">
      <IMG src="gfx/GEDI.png" alt="LOVD - Leiden Open Variation Database" width="404" height="100">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">The Genetic Eye Disorder (GEDI) Variation Database</H2>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.3.0 Build 08 [ <A href="status">Current LOVD status</A> ]<BR>
      <A href="users?register"><B>Register as submitter</B></A> | <A href="login"><B>Log in</B></A>
    </TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('gfx/tab_fill.png'); background-repeat : repeat-x;">
      <IMG src="gfx/tab_0F.png" alt="" width="25" height="25" align="left">
      <A href="genes"><IMG src="gfx/tab_genes_F.png" alt="View all genes" id="tab_genes" width="44" height="25" align="left"></A>
      <IMG src="gfx/tab_FB.png" alt="" width="25" height="25" align="left">
      <A href="transcripts"><IMG src="gfx/tab_transcripts_B.png" alt="View transcripts" id="tab_transcripts" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="variants"><IMG src="gfx/tab_variants_B.png" alt="View variants" id="tab_variants" width="58" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="individuals"><IMG src="gfx/tab_individuals_B.png" alt="View individuals" id="tab_individuals" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="diseases"><IMG src="gfx/tab_diseases_B.png" alt="View diseases" id="tab_diseases" width="62" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="screenings"><IMG src="gfx/tab_screenings_B.png" alt="View screenings" id="tab_screenings" width="78" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="submit"><IMG src="gfx/tab_submit_B.png" alt="Submit new data" id="tab_submit" width="53" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="docs"><IMG src="gfx/tab_docs_B.png" alt="LOVD documentation" id="tab_docs" width="110" height="25" align="left"></A>
      <IMG src="gfx/tab_B0.png" alt="" width="25" height="25" align="left">
    </TD>
  </TR>
</TABLE>

<IMG src="gfx/trans.png" alt="" width="792" height="0">

<!-- Start drop down menu definitions -->
<UL id="menu_tab_genes" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/genes"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genes</A></LI>
</UL>

<UL id="menu_tab_transcripts" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/transcripts"><SPAN class="icon" style="background-image: url(gfx/menu_transcripts.png);"></SPAN>View all transcripts</A></LI>
</UL>

<UL id="menu_tab_variants" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/variants"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genomic variants</A></LI>
  <LI class="icon"><A href="/GEDI/variants/in_gene"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all variants affecting transcripts</A></LI>
</UL>

<UL id="menu_tab_individuals" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/individuals"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all individuals</A></LI>
</UL>

<UL id="menu_tab_diseases" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/diseases"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all diseases</A></LI>
</UL>

<UL id="menu_tab_screenings" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/screenings"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all screenings</A></LI>
</UL>

<UL id="menu_tab_submit" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/submit"><SPAN class="icon" style="background-image: url(gfx/plus.png);"></SPAN>Submit new data</A></LI>
</UL>


<SCRIPT type="text/javascript">
  $(function(){
    var aMenuOptions = {
        widthOverflowOffset: 0,
        heightOverflowOffset: 1,
        startLeftOffset: -20,
        event: "mouseover",
        openBelowContext: true,
        autoHide: true,
        delay: 100,
        onSelect: function(e, context){
            if($(this).hasClass("disabled"))
            {
                return false;
            } else {
                window.location = $(this).find("a").attr("href");
                return false;
            }
        }
    };
    $('#tab_genes').jeegoocontext('menu_tab_genes', aMenuOptions);
    $('#tab_transcripts').jeegoocontext('menu_tab_transcripts', aMenuOptions);
    $('#tab_variants').jeegoocontext('menu_tab_variants', aMenuOptions);
    $('#tab_individuals').jeegoocontext('menu_tab_individuals', aMenuOptions);
    $('#tab_diseases').jeegoocontext('menu_tab_diseases', aMenuOptions);
    $('#tab_screenings').jeegoocontext('menu_tab_screenings', aMenuOptions);
    $('#tab_submit').jeegoocontext('menu_tab_submit', aMenuOptions);
  });
</SCRIPT>
<!-- End drop down menu definitions -->



<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD style="padding-top : 10px;">







      <H2 class="LOVD">View all genes</H2>

      <SCRIPT type="text/javascript" src="inc-js-viewlist.php"> </SCRIPT>
      <SCRIPT type="text/javascript" src="inc-js-tooltip.php"> </SCRIPT>
      <FORM action="genes" method="get" id="viewlistForm_Genes" style="margin : 0px;" onsubmit="return false;">
        <INPUT type="hidden" name="viewlistid" value="Genes">
        <INPUT type="hidden" name="object" value="Gene">
        <INPUT type="hidden" name="id" value="0">
        <INPUT type="hidden" name="order" value="id_,ASC">
        <INPUT type="hidden" name="skip[geneid]" value="geneid">

      <DIV id="viewlistDiv_Genes">
      <DIV id="viewlistLegend_Genes" title="Legend" style="display : none;">
        <H2 class="LOVD">Legend</H2>

        <I class="S11">Please note that a short description of a certain column can be displayed when you move your mouse cursor over the column's header and hold it still. Below, a more detailed description is shown per column.</I><BR><BR>

      </DIV>

      <SPAN class="S11" id="viewlistPageSplitText_Genes">
        298 entries on 3 pages. Showing entries 1 - 100.
      </SPAN>
      <TABLE border="0" cellpadding="0" cellspacing="3" class="pagesplit_nav">
        <TR>
          <TD style="border : 0px; cursor : default; padding-right : 10px;">
            <SELECT onchange="document.forms['viewlistForm_Genes'].page_size.value = this.value; document.forms['viewlistForm_Genes'].page.value = 1; lovd_AJAX_viewListSubmit('Genes');">
              <OPTION value="10">10 per page</OPTION>
              <OPTION value="25">25 per page</OPTION>
              <OPTION value="50">50 per page</OPTION>
              <OPTION value="100" selected>100 per page</OPTION>
              <OPTION value="250">250 per page</OPTION>
              <OPTION value="500">500 per page</OPTION>
              <OPTION value="1000">1000 per page</OPTION>
            </SELECT></TD>
          <TH class="inactive">&laquo; First</TH>
          <TH class="inactive">&#139; Prev</TH>
          <TD>&nbsp;&nbsp;&nbsp;</TD>
          <TD class="selected">1</TD>
          <TD class="num" onclick="lovd_AJAX_viewListGoToPage('Genes', 2);">2</TD>
          <TD class="num" onclick="lovd_AJAX_viewListGoToPage('Genes', 3);">3</TD>
          <TD>&nbsp;&nbsp;&nbsp;</TD>
          <TH onclick="lovd_AJAX_viewListGoToPage('Genes', 2);">Next &#155;</TH>
          <TH onclick="lovd_AJAX_viewListGoToPage('Genes', 3);">Last &raquo;</TH></TR></TABLE>

      <TABLE border="0" cellpadding="0" cellspacing="1" class="data" id="viewlistTable_Genes">
        <THEAD>
        <TR>
          <TH valign="top" class="ordered">
            <IMG src="gfx/trans.png" alt="" width="100" height="1" id="viewlistTable_Genes_colwidth_id_"><BR>
            <DIV onclick="document.forms['viewlistForm_Genes'].order.value='id_,DESC'; if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } lovd_AJAX_viewListSubmit('Genes');" style="position : relative;">
              <IMG src="gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Symbol&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_id_" value="" title="Symbol field should contain..." style="width : 94px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Genes\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="300" height="1" id="viewlistTable_Genes_colwidth_name"><BR>
            <DIV onclick="document.forms['viewlistForm_Genes'].order.value='name,ASC'; if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } lovd_AJAX_viewListSubmit('Genes');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Gene&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_name" value="" title="Gene field should contain..." style="width : 294px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Genes\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="50" height="1" id="viewlistTable_Genes_colwidth_chromosome"><BR>
            <DIV onclick="document.forms['viewlistForm_Genes'].order.value='chromosome,ASC'; if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } lovd_AJAX_viewListSubmit('Genes');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Chr&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_chromosome" value="" title="Chr field should contain..." style="width : 44px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Genes\')', 0); }"></TH>
          <TH valign="top">
            <IMG src="gfx/trans.png" alt="" width="70" height="1" id="viewlistTable_Genes_colwidth_chrom_band"><BR>Band<BR>
            <INPUT type="text" name="search_chrom_band" value="" title="Band field should contain..." style="width : 64px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Genes\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="90" height="1" id="viewlistTable_Genes_colwidth_transcripts"><BR>
            <DIV onclick="document.forms['viewlistForm_Genes'].order.value='transcripts,DESC'; if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } lovd_AJAX_viewListSubmit('Genes');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Transcripts&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_transcripts" value="" title="Transcripts field should contain..." style="width : 84px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Genes\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="70" height="1" id="viewlistTable_Genes_colwidth_variants"><BR>
            <DIV onclick="document.forms['viewlistForm_Genes'].order.value='variants,DESC'; if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } lovd_AJAX_viewListSubmit('Genes');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Variants&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_variants" value="" title="Variants field should contain..." style="width : 64px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Genes\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="70" height="1" id="viewlistTable_Genes_colwidth_uniq_variants"><BR>
            <DIV onclick="document.forms['viewlistForm_Genes'].order.value='uniq_variants,DESC'; if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } lovd_AJAX_viewListSubmit('Genes');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Unique&nbsp;variants&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_uniq_variants" value="" title="Unique variants field should contain..." style="width : 64px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Genes\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="110" height="1" id="viewlistTable_Genes_colwidth_updated_date_"><BR>
            <DIV onclick="document.forms['viewlistForm_Genes'].order.value='updated_date_,DESC'; if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } lovd_AJAX_viewListSubmit('Genes');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Last&nbsp;updated&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_updated_date_" value="" title="Last updated field should contain..." style="width : 104px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Genes\')', 0); }"></TH>
          <TH valign="top">
            <IMG src="gfx/trans.png" alt="" width="200" height="1" id="viewlistTable_Genes_colwidth_diseases_"><BR>Associated&nbsp;with&nbsp;diseases<BR>
            <INPUT type="text" name="search_diseases_" value="" title="Associated with diseases field should contain..." style="width : 194px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Genes'].page) { document.forms['viewlistForm_Genes'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Genes\')', 0); }"></TH></TR></THEAD>
        <TR class="data" id="ABCA4" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ABCA4';">
          <TD class="ordered"><A href="genes/ABCA4" class="hide">ABCA4</A></TD>
          <TD>ATP-binding cassette, sub-family A (ABC1), member 4</TD>
          <TD>1</TD>
          <TD>p22</TD>
          <TD>1</TD>
          <TD>54</TD>
          <TD>54</TD>
          <TD>2013-11-13</TD>
          <TD>CORD3, RP, RP19, STGD1</TD></TR>
        <TR class="data" id="ABCC6" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ABCC6';">
          <TD class="ordered"><A href="genes/ABCC6" class="hide">ABCC6</A></TD>
          <TD>ATP-binding cassette, sub-family C (CFTR/MRP), member 6</TD>
          <TD>16</TD>
          <TD>p13.11</TD>
          <TD>5</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ABHD12" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ABHD12';">
          <TD class="ordered"><A href="genes/ABHD12" class="hide">ABHD12</A></TD>
          <TD>abhydrolase domain containing 12</TD>
          <TD>20</TD>
          <TD>p11.21</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ADAM9" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ADAM9';">
          <TD class="ordered"><A href="genes/ADAM9" class="hide">ADAM9</A></TD>
          <TD>ADAM metallopeptidase domain 9</TD>
          <TD>8</TD>
          <TD>p11.23</TD>
          <TD>4</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ADAMTS18" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ADAMTS18';">
          <TD class="ordered"><A href="genes/ADAMTS18" class="hide">ADAMTS18</A></TD>
          <TD>ADAM metallopeptidase with thrombospondin type 1 motif, 18</TD>
          <TD>16</TD>
          <TD>q23</TD>
          <TD>1</TD>
          <TD>5</TD>
          <TD>5</TD>
          <TD>2013-12-11</TD>
          <TD>-</TD></TR>
        <TR class="data" id="AFG3L1P" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/AFG3L1P';">
          <TD class="ordered"><A href="genes/AFG3L1P" class="hide">AFG3L1P</A></TD>
          <TD>AFG3-like AAA ATPase 1, pseudogene</TD>
          <TD>16</TD>
          <TD>q24.3</TD>
          <TD>1</TD>
          <TD>4</TD>
          <TD>4</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="AHI1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/AHI1';">
          <TD class="ordered"><A href="genes/AHI1" class="hide">AHI1</A></TD>
          <TD>Abelson helper integration site 1</TD>
          <TD>6</TD>
          <TD>q23.2</TD>
          <TD>10</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="AIP" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/AIP';">
          <TD class="ordered"><A href="genes/AIP" class="hide">AIP</A></TD>
          <TD>aryl hydrocarbon receptor interacting protein</TD>
          <TD>11</TD>
          <TD>q13.3</TD>
          <TD>1</TD>
          <TD>65</TD>
          <TD>65</TD>
          <TD>2013-12-11</TD>
          <TD>-</TD></TR>
        <TR class="data" id="AIPL1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/AIPL1';">
          <TD class="ordered"><A href="genes/AIPL1" class="hide">AIPL1</A></TD>
          <TD>aryl hydrocarbon receptor interacting protein-like 1</TD>
          <TD>17</TD>
          <TD>p13.1</TD>
          <TD>8</TD>
          <TD>8</TD>
          <TD>8</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ALMS1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ALMS1';">
          <TD class="ordered"><A href="genes/ALMS1" class="hide">ALMS1</A></TD>
          <TD>Alstrom syndrome 1</TD>
          <TD>2</TD>
          <TD>p13.1</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ANKRD11" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ANKRD11';">
          <TD class="ordered"><A href="genes/ANKRD11" class="hide">ANKRD11</A></TD>
          <TD>ankyrin repeat domain 11</TD>
          <TD>16</TD>
          <TD>q24.3</TD>
          <TD>1</TD>
          <TD>5</TD>
          <TD>5</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ARL13B" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ARL13B';">
          <TD class="ordered"><A href="genes/ARL13B" class="hide">ARL13B</A></TD>
          <TD>ADP-ribosylation factor-like 13B</TD>
          <TD>3</TD>
          <TD>q11</TD>
          <TD>5</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ARL6" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ARL6';">
          <TD class="ordered"><A href="genes/ARL6" class="hide">ARL6</A></TD>
          <TD>ADP-ribosylation factor-like 6</TD>
          <TD>3</TD>
          <TD>q11.2</TD>
          <TD>3</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>RP</TD></TR>
        <TR class="data" id="ARMS2" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ARMS2';">
          <TD class="ordered"><A href="genes/ARMS2" class="hide">ARMS2</A></TD>
          <TD>age-related maculopathy susceptibility 2</TD>
          <TD>10</TD>
          <TD>q26.13</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ASIP" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ASIP';">
          <TD class="ordered"><A href="genes/ASIP" class="hide">ASIP</A></TD>
          <TD>agouti signaling protein</TD>
          <TD>20</TD>
          <TD>q11.2-q12</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ATOH7" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ATOH7';">
          <TD class="ordered"><A href="genes/ATOH7" class="hide">ATOH7</A></TD>
          <TD>atonal homolog 7 (Drosophila)</TD>
          <TD>10</TD>
          <TD>q22.2</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ATXN7" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ATXN7';">
          <TD class="ordered"><A href="genes/ATXN7" class="hide">ATXN7</A></TD>
          <TD>ataxin 7</TD>
          <TD>3</TD>
          <TD>p21.1-p12</TD>
          <TD>9</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="B3GALNT2" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/B3GALNT2';">
          <TD class="ordered"><A href="genes/B3GALNT2" class="hide">B3GALNT2</A></TD>
          <TD>beta-1,3-N-acetylgalactosaminyltransferase 2</TD>
          <TD>1</TD>
          <TD>q42.3</TD>
          <TD>1</TD>
          <TD>6</TD>
          <TD>6</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="B3GNT1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/B3GNT1';">
          <TD class="ordered"><A href="genes/B3GNT1" class="hide">B3GNT1</A></TD>
          <TD>UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1</TD>
          <TD>11</TD>
          <TD>q13.2</TD>
          <TD>1</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="BBS1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/BBS1';">
          <TD class="ordered"><A href="genes/BBS1" class="hide">BBS1</A></TD>
          <TD>Bardet-Biedl syndrome 1</TD>
          <TD>11</TD>
          <TD>q13</TD>
          <TD>5</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="BBS10" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/BBS10';">
          <TD class="ordered"><A href="genes/BBS10" class="hide">BBS10</A></TD>
          <TD>Bardet-Biedl syndrome 10</TD>
          <TD>12</TD>
          <TD>q21.2</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="BBS12" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/BBS12';">
          <TD class="ordered"><A href="genes/BBS12" class="hide">BBS12</A></TD>
          <TD>Bardet-Biedl syndrome 12</TD>
          <TD>4</TD>
          <TD>q27</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="BBS2" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/BBS2';">
          <TD class="ordered"><A href="genes/BBS2" class="hide">BBS2</A></TD>
          <TD>Bardet-Biedl syndrome 2</TD>
          <TD>16</TD>
          <TD>q21</TD>
          <TD>4</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="BBS4" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/BBS4';">
          <TD class="ordered"><A href="genes/BBS4" class="hide">BBS4</A></TD>
          <TD>Bardet-Biedl syndrome 4</TD>
          <TD>15</TD>
          <TD>q22.3-q23</TD>
          <TD>4</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="BBS5" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/BBS5';">
          <TD class="ordered"><A href="genes/BBS5" class="hide">BBS5</A></TD>
          <TD>Bardet-Biedl syndrome 5</TD>
          <TD>2</TD>
          <TD>q31</TD>
          <TD>3</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="BBS7" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/BBS7';">
          <TD class="ordered"><A href="genes/BBS7" class="hide">BBS7</A></TD>
          <TD>Bardet-Biedl syndrome 7</TD>
          <TD>4</TD>
          <TD>q27</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="BBS9" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/BBS9';">
          <TD class="ordered"><A href="genes/BBS9" class="hide">BBS9</A></TD>
          <TD>Bardet-Biedl syndrome 9</TD>
          <TD>7</TD>
          <TD>p14</TD>
          <TD>6</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="BEST1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/BEST1';">
          <TD class="ordered"><A href="genes/BEST1" class="hide">BEST1</A></TD>
          <TD>bestrophin 1</TD>
          <TD>11</TD>
          <TD>q12</TD>
          <TD>2</TD>
          <TD>11</TD>
          <TD>9</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="C10orf105" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/C10orf105';">
          <TD class="ordered"><A href="genes/C10orf105" class="hide">C10orf105</A></TD>
          <TD>chromosome 10 open reading frame 105</TD>
          <TD>10</TD>
          <TD>q22.1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="C1QTNF5" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/C1QTNF5';">
          <TD class="ordered"><A href="genes/C1QTNF5" class="hide">C1QTNF5</A></TD>
          <TD>C1q and tumor necrosis factor related protein 5</TD>
          <TD>11</TD>
          <TD>q23.3</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="C2" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/C2';">
          <TD class="ordered"><A href="genes/C2" class="hide">C2</A></TD>
          <TD>complement component 2</TD>
          <TD>6</TD>
          <TD>p21.3</TD>
          <TD>4</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="C2orf71" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/C2orf71';">
          <TD class="ordered"><A href="genes/C2orf71" class="hide">C2orf71</A></TD>
          <TD>chromosome 2 open reading frame 71</TD>
          <TD>2</TD>
          <TD>p23.2</TD>
          <TD>1</TD>
          <TD>3</TD>
          <TD>3</TD>
          <TD>N/A</TD>
          <TD>RP</TD></TR>
        <TR class="data" id="C3" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/C3';">
          <TD class="ordered"><A href="genes/C3" class="hide">C3</A></TD>
          <TD>complement component 3</TD>
          <TD>19</TD>
          <TD>p13.3-p13.2</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="C5orf42" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/C5orf42';">
          <TD class="ordered"><A href="genes/C5orf42" class="hide">C5orf42</A></TD>
          <TD>chromosome 5 open reading frame 42</TD>
          <TD>5</TD>
          <TD>p13.2</TD>
          <TD>11</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="C8orf37" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/C8orf37';">
          <TD class="ordered"><A href="genes/C8orf37" class="hide">C8orf37</A></TD>
          <TD>chromosome 8 open reading frame 37</TD>
          <TD>8</TD>
          <TD>q22.1</TD>
          <TD>2</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CA4" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CA4';">
          <TD class="ordered"><A href="genes/CA4" class="hide">CA4</A></TD>
          <TD>carbonic anhydrase IV</TD>
          <TD>17</TD>
          <TD>q23.1</TD>
          <TD>1</TD>
          <TD>3</TD>
          <TD>3</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CABP4" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CABP4';">
          <TD class="ordered"><A href="genes/CABP4" class="hide">CABP4</A></TD>
          <TD>calcium binding protein 4</TD>
          <TD>11</TD>
          <TD>q13.2</TD>
          <TD>4</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CACNA1F" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CACNA1F';">
          <TD class="ordered"><A href="genes/CACNA1F" class="hide">CACNA1F</A></TD>
          <TD>calcium channel, voltage-dependent, L type, alpha 1F subunit</TD>
          <TD>X</TD>
          <TD>p11.23</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CACNA2D4" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CACNA2D4';">
          <TD class="ordered"><A href="genes/CACNA2D4" class="hide">CACNA2D4</A></TD>
          <TD>calcium channel, voltage-dependent, alpha 2/delta subunit 4</TD>
          <TD>12</TD>
          <TD>p13.33</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CAPN5" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CAPN5';">
          <TD class="ordered"><A href="genes/CAPN5" class="hide">CAPN5</A></TD>
          <TD>calpain 5</TD>
          <TD>11</TD>
          <TD>q14</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CC2D2A" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CC2D2A';">
          <TD class="ordered"><A href="genes/CC2D2A" class="hide">CC2D2A</A></TD>
          <TD>coiled-coil and C2 domain containing 2A</TD>
          <TD>4</TD>
          <TD>p15.33</TD>
          <TD>7</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CDH23" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CDH23';">
          <TD class="ordered"><A href="genes/CDH23" class="hide">CDH23</A></TD>
          <TD>cadherin-related 23</TD>
          <TD>10</TD>
          <TD>q22.1</TD>
          <TD>9</TD>
          <TD>7</TD>
          <TD>7</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CDH3" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CDH3';">
          <TD class="ordered"><A href="genes/CDH3" class="hide">CDH3</A></TD>
          <TD>cadherin 3, type 1, P-cadherin (placental)</TD>
          <TD>16</TD>
          <TD>q22.1</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CDHR1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CDHR1';">
          <TD class="ordered"><A href="genes/CDHR1" class="hide">CDHR1</A></TD>
          <TD>cadherin-related family member 1</TD>
          <TD>10</TD>
          <TD>q23.1</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>RP</TD></TR>
        <TR class="data" id="CDK10" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CDK10';">
          <TD class="ordered"><A href="genes/CDK10" class="hide">CDK10</A></TD>
          <TD>cyclin-dependent kinase 10</TD>
          <TD>16</TD>
          <TD>q24.3</TD>
          <TD>1</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CDKL5" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CDKL5';">
          <TD class="ordered"><A href="genes/CDKL5" class="hide">CDKL5</A></TD>
          <TD>cyclin-dependent kinase-like 5</TD>
          <TD>X</TD>
          <TD>p22</TD>
          <TD>1</TD>
          <TD>11</TD>
          <TD>11</TD>
          <TD>2013-12-11</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CENPBD1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CENPBD1';">
          <TD class="ordered"><A href="genes/CENPBD1" class="hide">CENPBD1</A></TD>
          <TD>CENPB DNA-binding domains containing 1</TD>
          <TD>16</TD>
          <TD>q24.3</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CEP164" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CEP164';">
          <TD class="ordered"><A href="genes/CEP164" class="hide">CEP164</A></TD>
          <TD>centrosomal protein 164kDa</TD>
          <TD>11</TD>
          <TD>q23.3</TD>
          <TD>12</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CEP290" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CEP290';">
          <TD class="ordered"><A href="genes/CEP290" class="hide">CEP290</A></TD>
          <TD>centrosomal protein 290kDa</TD>
          <TD>12</TD>
          <TD>q21.33</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CEP41" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CEP41';">
          <TD class="ordered"><A href="genes/CEP41" class="hide">CEP41</A></TD>
          <TD>centrosomal protein 41kDa</TD>
          <TD>7</TD>
          <TD>q32</TD>
          <TD>5</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CERKL" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CERKL';">
          <TD class="ordered"><A href="genes/CERKL" class="hide">CERKL</A></TD>
          <TD>ceramide kinase-like</TD>
          <TD>2</TD>
          <TD>q31.3</TD>
          <TD>7</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>N/A</TD>
          <TD>RP</TD></TR>
        <TR class="data" id="CFB" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CFB';">
          <TD class="ordered"><A href="genes/CFB" class="hide">CFB</A></TD>
          <TD>complement factor B</TD>
          <TD>6</TD>
          <TD>p21.3</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CFH" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CFH';">
          <TD class="ordered"><A href="genes/CFH" class="hide">CFH</A></TD>
          <TD>complement factor H</TD>
          <TD>1</TD>
          <TD>q32</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>2013-11-09</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CHM" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CHM';">
          <TD class="ordered"><A href="genes/CHM" class="hide">CHM</A></TD>
          <TD>choroideremia (Rab escort protein 1)</TD>
          <TD>X</TD>
          <TD>q21.1-q21.3</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CHMP1A" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CHMP1A';">
          <TD class="ordered"><A href="genes/CHMP1A" class="hide">CHMP1A</A></TD>
          <TD>charged multivesicular body protein 1A</TD>
          <TD>16</TD>
          <TD>q24.3</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CIB2" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CIB2';">
          <TD class="ordered"><A href="genes/CIB2" class="hide">CIB2</A></TD>
          <TD>calcium and integrin binding family member 2</TD>
          <TD>15</TD>
          <TD>q24</TD>
          <TD>6</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>614869</TD></TR>
        <TR class="data" id="CLN3" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CLN3';">
          <TD class="ordered"><A href="genes/CLN3" class="hide">CLN3</A></TD>
          <TD>ceroid-lipofuscinosis, neuronal 3</TD>
          <TD>16</TD>
          <TD>p12</TD>
          <TD>5</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CLN5" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CLN5';">
          <TD class="ordered"><A href="genes/CLN5" class="hide">CLN5</A></TD>
          <TD>ceroid-lipofuscinosis, neuronal 5</TD>
          <TD>13</TD>
          <TD>q21.2-q32</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CLN6" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CLN6';">
          <TD class="ordered"><A href="genes/CLN6" class="hide">CLN6</A></TD>
          <TD>ceroid-lipofuscinosis, neuronal 6, late infantile, variant</TD>
          <TD>15</TD>
          <TD>q23</TD>
          <TD>5</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CLN8" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CLN8';">
          <TD class="ordered"><A href="genes/CLN8" class="hide">CLN8</A></TD>
          <TD>ceroid-lipofuscinosis, neuronal 8 (epilepsy, progressive with mental retardation)</TD>
          <TD>8</TD>
          <TD>p23.3</TD>
          <TD>9</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CLRN1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CLRN1';">
          <TD class="ordered"><A href="genes/CLRN1" class="hide">CLRN1</A></TD>
          <TD>clarin 1</TD>
          <TD>3</TD>
          <TD>q21-q25</TD>
          <TD>3</TD>
          <TD>9</TD>
          <TD>8</TD>
          <TD>N/A</TD>
          <TD>RP</TD></TR>
        <TR class="data" id="CNGA1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CNGA1';">
          <TD class="ordered"><A href="genes/CNGA1" class="hide">CNGA1</A></TD>
          <TD>cyclic nucleotide gated channel alpha 1</TD>
          <TD>4</TD>
          <TD>p12</TD>
          <TD>4</TD>
          <TD>4</TD>
          <TD>4</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CNGA3" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CNGA3';">
          <TD class="ordered"><A href="genes/CNGA3" class="hide">CNGA3</A></TD>
          <TD>cyclic nucleotide gated channel alpha 3</TD>
          <TD>2</TD>
          <TD>q11.2</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CNGB1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CNGB1';">
          <TD class="ordered"><A href="genes/CNGB1" class="hide">CNGB1</A></TD>
          <TD>cyclic nucleotide gated channel beta 1</TD>
          <TD>16</TD>
          <TD>q13</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CNGB3" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CNGB3';">
          <TD class="ordered"><A href="genes/CNGB3" class="hide">CNGB3</A></TD>
          <TD>cyclic nucleotide gated channel beta 3</TD>
          <TD>8</TD>
          <TD>q21.3</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CNNM4" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CNNM4';">
          <TD class="ordered"><A href="genes/CNNM4" class="hide">CNNM4</A></TD>
          <TD>cyclin M4</TD>
          <TD>2</TD>
          <TD>q11.2</TD>
          <TD>1</TD>
          <TD>5</TD>
          <TD>5</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="COL11A1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/COL11A1';">
          <TD class="ordered"><A href="genes/COL11A1" class="hide">COL11A1</A></TD>
          <TD>collagen, type XI, alpha 1</TD>
          <TD>1</TD>
          <TD>p21</TD>
          <TD>4</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="COL2A1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/COL2A1';">
          <TD class="ordered"><A href="genes/COL2A1" class="hide">COL2A1</A></TD>
          <TD>collagen, type II, alpha 1</TD>
          <TD>12</TD>
          <TD>q12-q13.2</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="COL9A1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/COL9A1';">
          <TD class="ordered"><A href="genes/COL9A1" class="hide">COL9A1</A></TD>
          <TD>collagen, type IX, alpha 1</TD>
          <TD>6</TD>
          <TD>q13</TD>
          <TD>2</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CPNE7" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CPNE7';">
          <TD class="ordered"><A href="genes/CPNE7" class="hide">CPNE7</A></TD>
          <TD>copine VII</TD>
          <TD>16</TD>
          <TD>q24.3</TD>
          <TD>1</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CRB1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CRB1';">
          <TD class="ordered"><A href="genes/CRB1" class="hide">CRB1</A></TD>
          <TD>crumbs homolog 1 (Drosophila)</TD>
          <TD>1</TD>
          <TD>q31-q32.1</TD>
          <TD>6</TD>
          <TD>9</TD>
          <TD>9</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CRX" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CRX';">
          <TD class="ordered"><A href="genes/CRX" class="hide">CRX</A></TD>
          <TD>cone-rod homeobox</TD>
          <TD>19</TD>
          <TD>q13.3</TD>
          <TD>3</TD>
          <TD>5</TD>
          <TD>3</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CTC1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CTC1';">
          <TD class="ordered"><A href="genes/CTC1" class="hide">CTC1</A></TD>
          <TD>CTS telomere maintenance complex component 1</TD>
          <TD>17</TD>
          <TD>p13.1</TD>
          <TD>1</TD>
          <TD>10</TD>
          <TD>10</TD>
          <TD>2013-12-11</TD>
          <TD>-</TD></TR>
        <TR class="data" id="CYP1B1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CYP1B1';">
          <TD class="ordered"><A href="genes/CYP1B1" class="hide">CYP1B1</A></TD>
          <TD>cytochrome P450, family 1, subfamily B, polypeptide 1</TD>
          <TD>2</TD>
          <TD>p22.2</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>101400, 120200, 120430, 120970, 125250, 165300, 165550, 193220, 203100, 206900, 210750, 217080, 222300, 227220, 227240, 236670, 253280, 258660, 262300, 268100, 276900, 276901, 276902, 276904, 300476, 300600, 303700, 303800, 304020, 600977, 601067, 601152, 601800, 602083, 602093, 602849, 603649, 604393, 605472, 606943, 606952, 607155, 607476, 608051, 608194, 610024, 610282, 610283, 610356, 610381, 610478, 611131, 611383, 611742, 612657, 612775, 612989, 613093, 613150, 613153, 613154, 613156, 613180, 613660, 613809, 614456, 614500, 614504, 614643, 614800, 614830, 614869, 615041, 615181, 615249, 615287, 615350, 615352, 615374, 615491, CORD3, GLC1A, GLC3A, OPA1, POAG, RP, RP19, RP2, RP3, RP4, STGD1, STGD3, STGD4</TD></TR>
        <TR class="data" id="CYP4V2" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/CYP4V2';">
          <TD class="ordered"><A href="genes/CYP4V2" class="hide">CYP4V2</A></TD>
          <TD>cytochrome P450, family 4, subfamily V, polypeptide 2</TD>
          <TD>4</TD>
          <TD>q35.2</TD>
          <TD>2</TD>
          <TD>34</TD>
          <TD>34</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="DBNDD1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/DBNDD1';">
          <TD class="ordered"><A href="genes/DBNDD1" class="hide">DBNDD1</A></TD>
          <TD>dysbindin (dystrobrevin binding protein 1) domain containing 1</TD>
          <TD>16</TD>
          <TD>q24.3</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="DENND2A" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/DENND2A';">
          <TD class="ordered"><A href="genes/DENND2A" class="hide">DENND2A</A></TD>
          <TD>DENN/MADD domain containing 2A</TD>
          <TD>7</TD>
          <TD>q34</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="DFNB31" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/DFNB31';">
          <TD class="ordered"><A href="genes/DFNB31" class="hide">DFNB31</A></TD>
          <TD>deafness, autosomal recessive 31</TD>
          <TD>9</TD>
          <TD>q32</TD>
          <TD>7</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="DHDDS" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/DHDDS';">
          <TD class="ordered"><A href="genes/DHDDS" class="hide">DHDDS</A></TD>
          <TD>dehydrodolichyl diphosphate synthase</TD>
          <TD>1</TD>
          <TD>p35.3</TD>
          <TD>4</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="DPEP1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/DPEP1';">
          <TD class="ordered"><A href="genes/DPEP1" class="hide">DPEP1</A></TD>
          <TD>dipeptidase 1 (renal)</TD>
          <TD>16</TD>
          <TD>q24</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="EFEMP1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/EFEMP1';">
          <TD class="ordered"><A href="genes/EFEMP1" class="hide">EFEMP1</A></TD>
          <TD>EGF containing fibulin-like extracellular matrix protein 1</TD>
          <TD>2</TD>
          <TD>p16</TD>
          <TD>2</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ELOVL4" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ELOVL4';">
          <TD class="ordered"><A href="genes/ELOVL4" class="hide">ELOVL4</A></TD>
          <TD>ELOVL fatty acid elongase 4</TD>
          <TD>6</TD>
          <TD>q14</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-10</TD>
          <TD>STGD3</TD></TR>
        <TR class="data" id="ERCC6" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ERCC6';">
          <TD class="ordered"><A href="genes/ERCC6" class="hide">ERCC6</A></TD>
          <TD>excision repair cross-complementing rodent repair deficiency, complementation group 6</TD>
          <TD>10</TD>
          <TD>q11</TD>
          <TD>4</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="ESRRG" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/ESRRG';">
          <TD class="ordered"><A href="genes/ESRRG" class="hide">ESRRG</A></TD>
          <TD>estrogen-related receptor gamma</TD>
          <TD>1</TD>
          <TD>q41</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="EYS" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/EYS';">
          <TD class="ordered"><A href="genes/EYS" class="hide">EYS</A></TD>
          <TD>eyes shut homolog (Drosophila)</TD>
          <TD>6</TD>
          <TD>q12</TD>
          <TD>3</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FAM161A" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FAM161A';">
          <TD class="ordered"><A href="genes/FAM161A" class="hide">FAM161A</A></TD>
          <TD>family with sequence similarity 161, member A</TD>
          <TD>2</TD>
          <TD>p15</TD>
          <TD>3</TD>
          <TD>5</TD>
          <TD>5</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FAM66B" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FAM66B';">
          <TD class="ordered"><A href="genes/FAM66B" class="hide">FAM66B</A></TD>
          <TD>family with sequence similarity 66, member B</TD>
          <TD>8</TD>
          <TD>p23.1</TD>
          <TD>1</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FAM66E" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FAM66E';">
          <TD class="ordered"><A href="genes/FAM66E" class="hide">FAM66E</A></TD>
          <TD>family with sequence similarity 66, member E</TD>
          <TD>8</TD>
          <TD>p23.1</TD>
          <TD>1</TD>
          <TD>2</TD>
          <TD>2</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FAM78B" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FAM78B';">
          <TD class="ordered"><A href="genes/FAM78B" class="hide">FAM78B</A></TD>
          <TD>family with sequence similarity 78, member B</TD>
          <TD>1</TD>
          <TD>q24.1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FANCA" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FANCA';">
          <TD class="ordered"><A href="genes/FANCA" class="hide">FANCA</A></TD>
          <TD>Fanconi anemia, complementation group A</TD>
          <TD>16</TD>
          <TD>q24.3</TD>
          <TD>1</TD>
          <TD>6</TD>
          <TD>6</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FBLN5" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FBLN5';">
          <TD class="ordered"><A href="genes/FBLN5" class="hide">FBLN5</A></TD>
          <TD>fibulin 5</TD>
          <TD>14</TD>
          <TD>q31</TD>
          <TD>1</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FBXL17" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FBXL17';">
          <TD class="ordered"><A href="genes/FBXL17" class="hide">FBXL17</A></TD>
          <TD>F-box and leucine-rich repeat protein 17</TD>
          <TD>5</TD>
          <TD>q21.3</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FGFR3" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FGFR3';">
          <TD class="ordered"><A href="genes/FGFR3" class="hide">FGFR3</A></TD>
          <TD>fibroblast growth factor receptor 3</TD>
          <TD>4</TD>
          <TD>p16.3</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FKRP" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FKRP';">
          <TD class="ordered"><A href="genes/FKRP" class="hide">FKRP</A></TD>
          <TD>fukutin related protein</TD>
          <TD>19</TD>
          <TD>q13.32</TD>
          <TD>1</TD>
          <TD>3</TD>
          <TD>3</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FKTN" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FKTN';">
          <TD class="ordered"><A href="genes/FKTN" class="hide">FKTN</A></TD>
          <TD>fukutin</TD>
          <TD>9</TD>
          <TD>q31-q33</TD>
          <TD>1</TD>
          <TD>5</TD>
          <TD>5</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FLVCR1" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FLVCR1';">
          <TD class="ordered"><A href="genes/FLVCR1" class="hide">FLVCR1</A></TD>
          <TD>feline leukemia virus subgroup C cellular receptor 1</TD>
          <TD>1</TD>
          <TD>q32.3</TD>
          <TD>1</TD>
          <TD>3</TD>
          <TD>3</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FSCN2" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FSCN2';">
          <TD class="ordered"><A href="genes/FSCN2" class="hide">FSCN2</A></TD>
          <TD>fascin homolog 2, actin-bundling protein, retinal (Strongylocentrotus purpuratus)</TD>
          <TD>17</TD>
          <TD>q25</TD>
          <TD>4</TD>
          <TD>0</TD>
          <TD>0</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="FZD4" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/FZD4';">
          <TD class="ordered"><A href="genes/FZD4" class="hide">FZD4</A></TD>
          <TD>frizzled family receptor 4</TD>
          <TD>11</TD>
          <TD>q14-q21</TD>
          <TD>1</TD>
          <TD>6</TD>
          <TD>6</TD>
          <TD>N/A</TD>
          <TD>-</TD></TR>
        <TR class="data" id="GAS8" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/GAS8';">
          <TD class="ordered"><A href="genes/GAS8" class="hide">GAS8</A></TD>
          <TD>growth arrest-specific 8</TD>
          <TD>16</TD>
          <TD>q24.3</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-11-19</TD>
          <TD>-</TD></TR>
        <TR class="data" id="GIGYF2" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/genes/GIGYF2';">
          <TD class="ordered"><A href="genes/GIGYF2" class="hide">GIGYF2</A></TD>
          <TD>GRB10 interacting GYF protein 2</TD>
          <TD>2</TD>
          <TD>q37.1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>1</TD>
          <TD>2013-12-11</TD>
          <TD>-</TD></TR></TABLE>
        <INPUT type="hidden" name="total" value="298" disabled>
        <INPUT type="hidden" name="page_size" value="100">
        <INPUT type="hidden" name="page" value="1">

      <TABLE border="0" cellpadding="0" cellspacing="3" class="pagesplit_nav">
        <TR>
          <TD style="border : 0px; cursor : default; padding-right : 10px;">
            <SELECT onchange="document.forms['viewlistForm_Genes'].page_size.value = this.value; document.forms['viewlistForm_Genes'].page.value = 1; lovd_AJAX_viewListSubmit('Genes');">
              <OPTION value="10">10 per page</OPTION>
              <OPTION value="25">25 per page</OPTION>
              <OPTION value="50">50 per page</OPTION>
              <OPTION value="100" selected>100 per page</OPTION>
              <OPTION value="250">250 per page</OPTION>
              <OPTION value="500">500 per page</OPTION>
              <OPTION value="1000">1000 per page</OPTION>
            </SELECT></TD>
          <TH class="inactive">&laquo; First</TH>
          <TH class="inactive">&#139; Prev</TH>
          <TD>&nbsp;&nbsp;&nbsp;</TD>
          <TD class="selected">1</TD>
          <TD class="num" onclick="lovd_AJAX_viewListGoToPage('Genes', 2);">2</TD>
          <TD class="num" onclick="lovd_AJAX_viewListGoToPage('Genes', 3);">3</TD>
          <TD>&nbsp;&nbsp;&nbsp;</TD>
          <TH onclick="lovd_AJAX_viewListGoToPage('Genes', 2);">Next &#155;</TH>
          <TH onclick="lovd_AJAX_viewListGoToPage('Genes', 3);">Last &raquo;</TH></TR></TABLE>

      </DIV></FORM><BR>
      <SCRIPT type="text/javascript">
        // This has to be run when the document has finished loading everything, because only then can it get the proper width from IE7 and lower!
        $( function () {lovd_stretchInputs('Genes');});
        check_list['Genes'] = [];
      </SCRIPT>










    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/3.0/" target="_blank">LOVD v.3.0</A> Build 08<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_update_error_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>
<SCRIPT type="text/javascript">
  <!--

function lovd_mapVariants ()
{
    // This function requests the script that will do the actual work.

    // First unbind any onclick handlers on the status image.
    $("#mapping_progress").unbind();

    // Now request the script.
    $.get("ajax/map_variants.php", function (sResponse)
        {
            // The server responded successfully. Let's see what he's saying.
            aResponse = sResponse.split("\t");
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_" + aResponse[1] + (aResponse[1] == "preparing"? ".gif" : ".png"), "title": aResponse[2]});

            if (sResponse.indexOf("Notice") >= 0 || sResponse.indexOf("Warning") >= 0 || sResponse.indexOf("Error") >= 0 || sResponse.indexOf("Fatal") >= 0) {
                // Something went wrong while processing the request, don't try again.
                $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sResponse});
            } else if (aResponse[0] == "1") {
                // More variants to map. Re-call.
                setTimeout("lovd_mapVariants()", 50);
            } else {
                // No more variants to map. But allow the user to try.
                $("#mapping_progress").click(lovd_mapVariants);
            }
        }
    ).fail(function (oObject, sStatus)
        {
            // Something went wrong while contacting the server, don't try again.
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sStatus});
        }
    );
}
setTimeout("lovd_mapVariants()", 500);
  // -->
</SCRIPT>

</BODY>
</HTML>
"""

BBS1_GENE_HOMEPAGE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>View gene BBS1 - The Genetic Eye Disorder (GEDI) Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <META name="author" content="LOVD development team, LUMC, Netherlands">
  <META name="generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <BASE href="http://mseqdr.lumc.edu/GEDI/">
  <LINK rel="stylesheet" type="text/css" href="styles.css">
  <LINK rel="shortcut icon" href="favicon.ico" type="image/x-icon">

  <SCRIPT type="text/javascript" src="inc-js-openwindow.php"> </SCRIPT>
  <SCRIPT type="text/javascript" src="inc-js-toggle-visibility.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery.min.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery-ui.custom.min.js"> </SCRIPT>

  <SCRIPT type="text/javascript">
    <!--

    var sURL = "/GEDI/genes/{{GENE}}";
    function lovd_switchGeneInline () {
      var sForm = '<FORM action="" id="SelectGeneDBInline" method="get" style="margin : 0px;" onsubmit="document.location.href=(sURL.replace(\'{{GENE}}\', $(this).children(\'select\').val())); return false;"><SELECT name="select_db" onchange="$(this).parent().submit();"><OPTION value="ABCA4">ABCA4 (ATP-binding cassette, sub-family A (ABC1), member 4)</OPTION><OPTION value="ABCC6">ABCC6 (ATP-binding cassette, sub-family C (CFTR/MRP), member 6)</OPTION><OPTION value="ABHD12">ABHD12 (abhydrolase domain containing 12)</OPTION><OPTION value="ADAM9">ADAM9 (ADAM metallopeptidase domain 9)</OPTION><OPTION value="ADAMTS18">ADAMTS18 (ADAM metallopeptidase with thrombospondin type 1 motif, 18)</OPTION><OPTION value="AFG3L1P">AFG3L1P (AFG3-like AAA ATPase 1, pseudogene)</OPTION><OPTION value="AHI1">AHI1 (Abelson helper integration site 1)</OPTION><OPTION value="AIP">AIP (aryl hydrocarbon receptor interacting protein)</OPTION><OPTION value="AIPL1">AIPL1 (aryl hydrocarbon receptor interacting protein-like 1)</OPTION><OPTION value="ALMS1">ALMS1 (Alstrom syndrome 1)</OPTION><OPTION value="ANKRD11">ANKRD11 (ankyrin repeat domain 11)</OPTION><OPTION value="ARL13B">ARL13B (ADP-ribosylation factor-like 13B)</OPTION><OPTION value="ARL6">ARL6 (ADP-ribosylation factor-like 6)</OPTION><OPTION value="ARMS2">ARMS2 (age-related maculopathy susceptibility 2)</OPTION><OPTION value="ASIP">ASIP (agouti signaling protein)</OPTION><OPTION value="ATOH7">ATOH7 (atonal homolog 7 (Drosophila))</OPTION><OPTION value="ATXN7">ATXN7 (ataxin 7)</OPTION><OPTION value="B3GALNT2">B3GALNT2 (beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION><OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION><OPTION value="BBS1" selected>BBS1 (Bardet-Biedl syndrome 1)</OPTION><OPTION value="BBS10">BBS10 (Bardet-Biedl syndrome 10)</OPTION><OPTION value="BBS12">BBS12 (Bardet-Biedl syndrome 12)</OPTION><OPTION value="BBS2">BBS2 (Bardet-Biedl syndrome 2)</OPTION><OPTION value="BBS4">BBS4 (Bardet-Biedl syndrome 4)</OPTION><OPTION value="BBS5">BBS5 (Bardet-Biedl syndrome 5)</OPTION><OPTION value="BBS7">BBS7 (Bardet-Biedl syndrome 7)</OPTION><OPTION value="BBS9">BBS9 (Bardet-Biedl syndrome 9)</OPTION><OPTION value="BEST1">BEST1 (bestrophin 1)</OPTION><OPTION value="C10orf105">C10orf105 (chromosome 10 open reading frame 105)</OPTION><OPTION value="C1QTNF5">C1QTNF5 (C1q and tumor necrosis factor related protein 5)</OPTION><OPTION value="C2">C2 (complement component 2)</OPTION><OPTION value="C2orf71">C2orf71 (chromosome 2 open reading frame 71)</OPTION><OPTION value="C3">C3 (complement component 3)</OPTION><OPTION value="C5orf42">C5orf42 (chromosome 5 open reading frame 42)</OPTION><OPTION value="C8orf37">C8orf37 (chromosome 8 open reading frame 37)</OPTION><OPTION value="CA4">CA4 (carbonic anhydrase IV)</OPTION><OPTION value="CABP4">CABP4 (calcium binding protein 4)</OPTION><OPTION value="CACNA1F">CACNA1F (calcium channel, voltage-dependent, L type, alpha 1F subunit)</OPTION><OPTION value="CACNA2D4">CACNA2D4 (calcium channel, voltage-dependent, alpha 2/delta subunit 4)</OPTION><OPTION value="CAPN5">CAPN5 (calpain 5)</OPTION><OPTION value="CC2D2A">CC2D2A (coiled-coil and C2 domain containing 2A)</OPTION><OPTION value="CDH23">CDH23 (cadherin-related 23)</OPTION><OPTION value="CDH3">CDH3 (cadherin 3, type 1, P-cadherin (placental))</OPTION><OPTION value="CDHR1">CDHR1 (cadherin-related family member 1)</OPTION><OPTION value="CDK10">CDK10 (cyclin-dependent kinase 10)</OPTION><OPTION value="CDKL5">CDKL5 (cyclin-dependent kinase-like 5)</OPTION><OPTION value="CENPBD1">CENPBD1 (CENPB DNA-binding domains containing 1)</OPTION><OPTION value="CEP164">CEP164 (centrosomal protein 164kDa)</OPTION><OPTION value="CEP290">CEP290 (centrosomal protein 290kDa)</OPTION><OPTION value="CEP41">CEP41 (centrosomal protein 41kDa)</OPTION><OPTION value="CERKL">CERKL (ceramide kinase-like)</OPTION><OPTION value="CFB">CFB (complement factor B)</OPTION><OPTION value="CFH">CFH (complement factor H)</OPTION><OPTION value="CHM">CHM (choroideremia (Rab escort protein 1))</OPTION><OPTION value="CHMP1A">CHMP1A (charged multivesicular body protein 1A)</OPTION><OPTION value="CIB2">CIB2 (calcium and integrin binding family member 2)</OPTION><OPTION value="CLN3">CLN3 (ceroid-lipofuscinosis, neuronal 3)</OPTION><OPTION value="CLN5">CLN5 (ceroid-lipofuscinosis, neuronal 5)</OPTION><OPTION value="CLN6">CLN6 (ceroid-lipofuscinosis, neuronal 6, late infantile, variant)</OPTION><OPTION value="CLN8">CLN8 (ceroid-lipofuscinosis, neuronal 8 (epilepsy, progressive with me...))</OPTION><OPTION value="CLRN1">CLRN1 (clarin 1)</OPTION><OPTION value="CNGA1">CNGA1 (cyclic nucleotide gated channel alpha 1)</OPTION><OPTION value="CNGA3">CNGA3 (cyclic nucleotide gated channel alpha 3)</OPTION><OPTION value="CNGB1">CNGB1 (cyclic nucleotide gated channel beta 1)</OPTION><OPTION value="CNGB3">CNGB3 (cyclic nucleotide gated channel beta 3)</OPTION><OPTION value="CNNM4">CNNM4 (cyclin M4)</OPTION><OPTION value="COL11A1">COL11A1 (collagen, type XI, alpha 1)</OPTION><OPTION value="COL2A1">COL2A1 (collagen, type II, alpha 1)</OPTION><OPTION value="COL9A1">COL9A1 (collagen, type IX, alpha 1)</OPTION><OPTION value="CPNE7">CPNE7 (copine VII)</OPTION><OPTION value="CRB1">CRB1 (crumbs homolog 1 (Drosophila))</OPTION><OPTION value="CRX">CRX (cone-rod homeobox)</OPTION><OPTION value="CTC1">CTC1 (CTS telomere maintenance complex component 1)</OPTION><OPTION value="CYP1B1">CYP1B1 (cytochrome P450, family 1, subfamily B, polypeptide 1)</OPTION><OPTION value="CYP4V2">CYP4V2 (cytochrome P450, family 4, subfamily V, polypeptide 2)</OPTION><OPTION value="DBNDD1">DBNDD1 (dysbindin (dystrobrevin binding protein 1) domain containing 1)</OPTION><OPTION value="DENND2A">DENND2A (DENN/MADD domain containing 2A)</OPTION><OPTION value="DFNB31">DFNB31 (deafness, autosomal recessive 31)</OPTION><OPTION value="DHDDS">DHDDS (dehydrodolichyl diphosphate synthase)</OPTION><OPTION value="DPEP1">DPEP1 (dipeptidase 1 (renal))</OPTION><OPTION value="EFEMP1">EFEMP1 (EGF containing fibulin-like extracellular matrix protein 1)</OPTION><OPTION value="ELOVL4">ELOVL4 (ELOVL fatty acid elongase 4)</OPTION><OPTION value="ERCC6">ERCC6 (excision repair cross-complementing rodent repair deficiency, co...)</OPTION><OPTION value="ESRRG">ESRRG (estrogen-related receptor gamma)</OPTION><OPTION value="EYS">EYS (eyes shut homolog (Drosophila))</OPTION><OPTION value="FAM161A">FAM161A (family with sequence similarity 161, member A)</OPTION><OPTION value="FAM66B">FAM66B (family with sequence similarity 66, member B)</OPTION><OPTION value="FAM66E">FAM66E (family with sequence similarity 66, member E)</OPTION><OPTION value="FAM78B">FAM78B (family with sequence similarity 78, member B)</OPTION><OPTION value="FANCA">FANCA (Fanconi anemia, complementation group A)</OPTION><OPTION value="FBLN5">FBLN5 (fibulin 5)</OPTION><OPTION value="FBXL17">FBXL17 (F-box and leucine-rich repeat protein 17)</OPTION><OPTION value="FGFR3">FGFR3 (fibroblast growth factor receptor 3)</OPTION><OPTION value="FKRP">FKRP (fukutin related protein)</OPTION><OPTION value="FKTN">FKTN (fukutin)</OPTION><OPTION value="FLVCR1">FLVCR1 (feline leukemia virus subgroup C cellular receptor 1)</OPTION><OPTION value="FSCN2">FSCN2 (fascin homolog 2, actin-bundling protein, retinal (Strongylocen...))</OPTION><OPTION value="FZD4">FZD4 (frizzled family receptor 4)</OPTION><OPTION value="GAS8">GAS8 (growth arrest-specific 8)</OPTION><OPTION value="GIGYF2">GIGYF2 (GRB10 interacting GYF protein 2)</OPTION><OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION><OPTION value="GNAT1">GNAT1 (guanine nucleotide binding protein (G protein), alpha transducin...)</OPTION><OPTION value="GNAT2">GNAT2 (guanine nucleotide binding protein (G protein), alpha transducin...)</OPTION><OPTION value="GNPTG">GNPTG (N-acetylglucosamine-1-phosphate transferase, gamma subunit)</OPTION><OPTION value="GPR143">GPR143 (G protein-coupled receptor 143)</OPTION><OPTION value="GPR179">GPR179 (G protein-coupled receptor 179)</OPTION><OPTION value="GPR98">GPR98 (G protein-coupled receptor 98)</OPTION><OPTION value="GRK1">GRK1 (G protein-coupled receptor kinase 1)</OPTION><OPTION value="GRM6">GRM6 (glutamate receptor, metabotropic 6)</OPTION><OPTION value="GRN">GRN (granulin)</OPTION><OPTION value="GUCA1A">GUCA1A (guanylate cyclase activator 1A (retina))</OPTION><OPTION value="GUCA1B">GUCA1B (guanylate cyclase activator 1B (retina))</OPTION><OPTION value="GUCY2D">GUCY2D (guanylate cyclase 2D, membrane (retina-specific))</OPTION><OPTION value="HARS">HARS (histidyl-tRNA synthetase)</OPTION><OPTION value="HERC2">HERC2 (HECT and RLD domain containing E3 ubiquitin protein ligase 2)</OPTION><OPTION value="HESX1">HESX1 (HESX homeobox 1)</OPTION><OPTION value="HMCN1">HMCN1 (hemicentin 1)</OPTION><OPTION value="HTRA1">HTRA1 (HtrA serine peptidase 1)</OPTION><OPTION value="IDH3B">IDH3B (isocitrate dehydrogenase 3 (NAD+) beta)</OPTION><OPTION value="IFT140">IFT140 (intraflagellar transport 140 homolog (Chlamydomonas))</OPTION><OPTION value="IFT80">IFT80 (intraflagellar transport 80 homolog (Chlamydomonas))</OPTION><OPTION value="IMPDH1">IMPDH1 (IMP (inosine 5\'-monophosphate) dehydrogenase 1)</OPTION><OPTION value="IMPG2">IMPG2 (interphotoreceptor matrix proteoglycan 2)</OPTION><OPTION value="INPP5E">INPP5E (inositol polyphosphate-5-phosphatase, 72 kDa)</OPTION><OPTION value="INVS">INVS (inversin)</OPTION><OPTION value="IQCB1">IQCB1 (IQ motif containing B1)</OPTION><OPTION value="IRF4">IRF4 (interferon regulatory factor 4)</OPTION><OPTION value="ISPD">ISPD (isoprenoid synthase domain containing)</OPTION><OPTION value="JAG1">JAG1 (jagged 1)</OPTION><OPTION value="KCNJ13">KCNJ13 (potassium inwardly-rectifying channel, subfamily J, member 13)</OPTION><OPTION value="KCNV2">KCNV2 (potassium channel, subfamily V, member 2)</OPTION><OPTION value="KCTD7">KCTD7 (potassium channel tetramerization domain containing 7)</OPTION><OPTION value="KIF11">KIF11 (kinesin family member 11)</OPTION><OPTION value="KLHL7">KLHL7 (kelch-like family member 7)</OPTION><OPTION value="LARGE">LARGE (like-glycosyltransferase)</OPTION><OPTION value="LCA5">LCA5 (Leber congenital amaurosis 5)</OPTION><OPTION value="LCAT">LCAT (lecithin-cholesterol acyltransferase)</OPTION><OPTION value="LRAT">LRAT (lecithin retinol acyltransferase (phosphatidylcholine--retinol O...))</OPTION><OPTION value="LRIT3">LRIT3 (leucine-rich repeat, immunoglobulin-like and transmembrane domai...)</OPTION><OPTION value="LRP1B">LRP1B (low density lipoprotein receptor-related protein 1B)</OPTION><OPTION value="LRP5">LRP5 (low density lipoprotein receptor-related protein 5)</OPTION><OPTION value="LZTFL1">LZTFL1 (leucine zipper transcription factor-like 1)</OPTION><OPTION value="MAK">MAK (male germ cell-associated kinase)</OPTION><OPTION value="MC1R">MC1R (melanocortin 1 receptor (alpha melanocyte stimulating hormone re...))</OPTION><OPTION value="MERTK">MERTK (c-mer proto-oncogene tyrosine kinase)</OPTION><OPTION value="MFN2">MFN2 (mitofusin 2)</OPTION><OPTION value="MFRP">MFRP (membrane frizzled-related protein)</OPTION><OPTION value="MFSD8">MFSD8 (major facilitator superfamily domain containing 8)</OPTION><OPTION value="MKKS">MKKS (McKusick-Kaufman syndrome)</OPTION><OPTION value="MKS1">MKS1 (Meckel syndrome, type 1)</OPTION><OPTION value="MSH4">MSH4 (mutS homolog 4)</OPTION><OPTION value="MTAP">MTAP (methylthioadenosine phosphorylase)</OPTION><OPTION value="MTTP">MTTP (microsomal triglyceride transfer protein)</OPTION><OPTION value="MYH9">MYH9 (myosin, heavy chain 9, non-muscle)</OPTION><OPTION value="MYO7A">MYO7A (myosin VIIA)</OPTION><OPTION value="MYPN">MYPN (myopalladin)</OPTION><OPTION value="NBAS">NBAS (neuroblastoma amplified sequence)</OPTION><OPTION value="NDP">NDP (Norrie disease (pseudoglioma))</OPTION><OPTION value="NEK4">NEK4 (NIMA-related kinase 4)</OPTION><OPTION value="NEK8">NEK8 (NIMA-related kinase 8)</OPTION><OPTION value="NMNAT1">NMNAT1 (nicotinamide nucleotide adenylyltransferase 1)</OPTION><OPTION value="NPHP1">NPHP1 (nephronophthisis 1 (juvenile))</OPTION><OPTION value="NPHP3">NPHP3 (nephronophthisis 3 (adolescent))</OPTION><OPTION value="NPHP4">NPHP4 (nephronophthisis 4)</OPTION><OPTION value="NPLOC4">NPLOC4 (nuclear protein localization 4 homolog (S. cerevisiae))</OPTION><OPTION value="NR2E3">NR2E3 (nuclear receptor subfamily 2, group E, member 3)</OPTION><OPTION value="NRL">NRL (neural retina leucine zipper)</OPTION><OPTION value="NUB1">NUB1 (negative regulator of ubiquitin-like proteins 1)</OPTION><OPTION value="NYX">NYX (nyctalopin)</OPTION><OPTION value="OAT">OAT (ornithine aminotransferase)</OPTION><OPTION value="OCA2">OCA2 (oculocutaneous albinism II)</OPTION><OPTION value="OFD1">OFD1 (oral-facial-digital syndrome 1)</OPTION><OPTION value="OPA1">OPA1 (optic atrophy 1 (autosomal dominant))</OPTION><OPTION value="OPA1-AS1">OPA1-AS1 (OPA1 antisense RNA 1)</OPTION><OPTION value="OPA3">OPA3 (optic atrophy 3 (autosomal recessive, with chorea and spastic pa...))</OPTION><OPTION value="OPN1LW">OPN1LW (opsin 1 (cone pigments), long-wave-sensitive)</OPTION><OPTION value="OPN1MW">OPN1MW (opsin 1 (cone pigments), medium-wave-sensitive)</OPTION><OPTION value="OPN1SW">OPN1SW (opsin 1 (cone pigments), short-wave-sensitive)</OPTION><OPTION value="OTX2">OTX2 (orthodenticle homeobox 2)</OPTION><OPTION value="PANK2">PANK2 (pantothenate kinase 2)</OPTION><OPTION value="PAX2">PAX2 (paired box 2)</OPTION><OPTION value="PAX6">PAX6 (paired box 6)</OPTION><OPTION value="PCDH15">PCDH15 (protocadherin-related 15)</OPTION><OPTION value="PDE6A">PDE6A (phosphodiesterase 6A, cGMP-specific, rod, alpha)</OPTION><OPTION value="PDE6B">PDE6B (phosphodiesterase 6B, cGMP-specific, rod, beta)</OPTION><OPTION value="PDE6C">PDE6C (phosphodiesterase 6C, cGMP-specific, cone, alpha prime)</OPTION><OPTION value="PDE6G">PDE6G (phosphodiesterase 6G, cGMP-specific, rod, gamma)</OPTION><OPTION value="PDE6H">PDE6H (phosphodiesterase 6H, cGMP-specific, cone, gamma)</OPTION><OPTION value="PDZD7">PDZD7 (PDZ domain containing 7)</OPTION><OPTION value="PEX1">PEX1 (peroxisomal biogenesis factor 1)</OPTION><OPTION value="PEX10">PEX10 (peroxisomal biogenesis factor 10)</OPTION><OPTION value="PEX14">PEX14 (peroxisomal biogenesis factor 14)</OPTION><OPTION value="PEX16">PEX16 (peroxisomal biogenesis factor 16)</OPTION><OPTION value="PEX19">PEX19 (peroxisomal biogenesis factor 19)</OPTION><OPTION value="PEX2">PEX2 (peroxisomal biogenesis factor 2)</OPTION><OPTION value="PEX5">PEX5 (peroxisomal biogenesis factor 5)</OPTION><OPTION value="PEX6">PEX6 (peroxisomal biogenesis factor 6)</OPTION><OPTION value="PEX7">PEX7 (peroxisomal biogenesis factor 7)</OPTION><OPTION value="PGK1">PGK1 (phosphoglycerate kinase 1)</OPTION><OPTION value="PHYH">PHYH (phytanoyl-CoA 2-hydroxylase)</OPTION><OPTION value="PITPNM3">PITPNM3 (PITPNM family member 3)</OPTION><OPTION value="PLA2G5">PLA2G5 (phospholipase A2, group V)</OPTION><OPTION value="POMGNT1">POMGNT1 (protein O-linked mannose N-acetylglucosaminyltransferase 1 (b...))</OPTION><OPTION value="POMT1">POMT1 (protein-O-mannosyltransferase 1)</OPTION><OPTION value="POMT2">POMT2 (protein-O-mannosyltransferase 2)</OPTION><OPTION value="PPT1">PPT1 (palmitoyl-protein thioesterase 1)</OPTION><OPTION value="PRCD">PRCD (progressive rod-cone degeneration)</OPTION><OPTION value="PRDM7">PRDM7 (PR domain containing 7)</OPTION><OPTION value="PROM1">PROM1 (prominin 1)</OPTION><OPTION value="PRPF3">PRPF3 (pre-mRNA processing factor 3)</OPTION><OPTION value="PRPF31">PRPF31 (pre-mRNA processing factor 31)</OPTION><OPTION value="PRPF6">PRPF6 (pre-mRNA processing factor 6)</OPTION><OPTION value="PRPF8">PRPF8 (pre-mRNA processing factor 8)</OPTION><OPTION value="PRPH2">PRPH2 (peripherin 2 (retinal degeneration, slow))</OPTION><OPTION value="RAB28">RAB28 (RAB28, member RAS oncogene family)</OPTION><OPTION value="RAX2">RAX2 (retina and anterior neural fold homeobox 2)</OPTION><OPTION value="RB1">RB1 (retinoblastoma 1)</OPTION><OPTION value="RBP3">RBP3 (retinol binding protein 3, interstitial)</OPTION><OPTION value="RBP4">RBP4 (retinol binding protein 4, plasma)</OPTION><OPTION value="RD3">RD3 (retinal degeneration 3)</OPTION><OPTION value="RDH12">RDH12 (retinol dehydrogenase 12 (all-trans/9-cis/11-cis))</OPTION><OPTION value="RDH5">RDH5 (retinol dehydrogenase 5 (11-cis/9-cis))</OPTION><OPTION value="RFTN1">RFTN1 (raftlin, lipid raft linker 1)</OPTION><OPTION value="RGR">RGR (retinal G protein coupled receptor)</OPTION><OPTION value="RGS9">RGS9 (regulator of G-protein signaling 9)</OPTION><OPTION value="RGS9BP">RGS9BP (regulator of G protein signaling 9 binding protein)</OPTION><OPTION value="RHO">RHO (rhodopsin)</OPTION><OPTION value="RIMS1">RIMS1 (regulating synaptic membrane exocytosis 1)</OPTION><OPTION value="RLBP1">RLBP1 (retinaldehyde binding protein 1)</OPTION><OPTION value="ROM1">ROM1 (retinal outer segment membrane protein 1)</OPTION><OPTION value="RP1">RP1 (retinitis pigmentosa 1 (autosomal dominant))</OPTION><OPTION value="RP1L1">RP1L1 (retinitis pigmentosa 1-like 1)</OPTION><OPTION value="RP2">RP2 (retinitis pigmentosa 2 (X-linked recessive))</OPTION><OPTION value="RP9">RP9 (retinitis pigmentosa 9 (autosomal dominant))</OPTION><OPTION value="RPE65">RPE65 (retinal pigment epithelium-specific protein 65kDa)</OPTION><OPTION value="RPGR">RPGR (retinitis pigmentosa GTPase regulator)</OPTION><OPTION value="RPGRIP1">RPGRIP1 (retinitis pigmentosa GTPase regulator interacting protein 1)</OPTION><OPTION value="RPGRIP1L">RPGRIP1L (RPGRIP1-like)</OPTION><OPTION value="RS1">RS1 (retinoschisin 1)</OPTION><OPTION value="SAG">SAG (S-antigen; retina and pineal gland (arrestin))</OPTION><OPTION value="SCFD2">SCFD2 (sec1 family domain containing 2)</OPTION><OPTION value="SDCCAG8">SDCCAG8 (serologically defined colon cancer antigen 8)</OPTION><OPTION value="SEMA4A">SEMA4A (sema domain, immunoglobulin domain (Ig), transmembrane domain ...)</OPTION><OPTION value="SLC12A4">SLC12A4 (solute carrier family 12 (potassium/chloride transporter), mem...)</OPTION><OPTION value="SLC24A1">SLC24A1 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC24A4">SLC24A4 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC24A5">SLC24A5 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC45A2">SLC45A2 (solute carrier family 45, member 2)</OPTION><OPTION value="SNRNP200">SNRNP200 (small nuclear ribonucleoprotein 200kDa (U5))</OPTION><OPTION value="SOX2">SOX2 (SRY (sex determining region Y)-box 2)</OPTION><OPTION value="SOX2-OT">SOX2-OT (SOX2 overlapping transcript (non-protein coding))</OPTION><OPTION value="SPATA2L">SPATA2L (spermatogenesis associated 2-like)</OPTION><OPTION value="SPATA7">SPATA7 (spermatogenesis associated 7)</OPTION><OPTION value="SPG7">SPG7 (spastic paraplegia 7 (pure and complicated autosomal recessive))</OPTION><OPTION value="SPIRE2">SPIRE2 (spire-type actin nucleation factor 2)</OPTION><OPTION value="TEAD1">TEAD1 (TEA domain family member 1 (SV40 transcriptional enhancer factor))</OPTION><OPTION value="TIMM8A">TIMM8A (translocase of inner mitochondrial membrane 8 homolog A (yeast))</OPTION><OPTION value="TIMP3">TIMP3 (TIMP metallopeptidase inhibitor 3)</OPTION><OPTION value="TLR3">TLR3 (toll-like receptor 3)</OPTION><OPTION value="TLR4">TLR4 (toll-like receptor 4)</OPTION><OPTION value="TMEM126A">TMEM126A (transmembrane protein 126A)</OPTION><OPTION value="TMEM231">TMEM231 (transmembrane protein 231)</OPTION><OPTION value="TMEM237">TMEM237 (transmembrane protein 237)</OPTION><OPTION value="TMEM5">TMEM5 (transmembrane protein 5)</OPTION><OPTION value="TMEM67">TMEM67 (transmembrane protein 67)</OPTION><OPTION value="TOPORS">TOPORS (topoisomerase I binding, arginine/serine-rich, E3 ubiquitin pro...)</OPTION><OPTION value="TPCN2">TPCN2 (two pore segment channel 2)</OPTION><OPTION value="TPP1">TPP1 (tripeptidyl peptidase I)</OPTION><OPTION value="TREX1">TREX1 (three prime repair exonuclease 1)</OPTION><OPTION value="TRIM32">TRIM32 (tripartite motif containing 32)</OPTION><OPTION value="TRPM1">TRPM1 (transient receptor potential cation channel, subfamily M, member 1)</OPTION><OPTION value="TSHR">TSHR (thyroid stimulating hormone receptor)</OPTION><OPTION value="TSPAN12">TSPAN12 (tetraspanin 12)</OPTION><OPTION value="TTC21B">TTC21B (tetratricopeptide repeat domain 21B)</OPTION><OPTION value="TTC3">TTC3 (tetratricopeptide repeat domain 3)</OPTION><OPTION value="TTC8">TTC8 (tetratricopeptide repeat domain 8)</OPTION><OPTION value="TTPA">TTPA (tocopherol (alpha) transfer protein)</OPTION><OPTION value="TTR">TTR (transthyretin)</OPTION><OPTION value="TUBGCP6">TUBGCP6 (tubulin, gamma complex associated protein 6)</OPTION><OPTION value="TULP1">TULP1 (tubby like protein 1)</OPTION><OPTION value="TWIST1">TWIST1 (twist family bHLH transcription factor 1)</OPTION><OPTION value="TYR">TYR (tyrosinase)</OPTION><OPTION value="TYRP1">TYRP1 (tyrosinase-related protein 1)</OPTION><OPTION value="UCHL1">UCHL1 (ubiquitin carboxyl-terminal esterase L1 (ubiquitin thiolesterase))</OPTION><OPTION value="UNC119">UNC119 (unc-119 homolog (C. elegans))</OPTION><OPTION value="USH1C">USH1C (Usher syndrome 1C (autosomal recessive, severe))</OPTION><OPTION value="USH1G">USH1G (Usher syndrome 1G (autosomal recessive))</OPTION><OPTION value="USH2A">USH2A (Usher syndrome 2A (autosomal recessive, mild))</OPTION><OPTION value="VCAN">VCAN (versican)</OPTION><OPTION value="VPS13B">VPS13B (vacuolar protein sorting 13 homolog B (yeast))</OPTION><OPTION value="WDPCP">WDPCP (WD repeat containing planar cell polarity effector)</OPTION><OPTION value="WDR19">WDR19 (WD repeat domain 19)</OPTION><OPTION value="WFS1">WFS1 (Wolfram syndrome 1 (wolframin))</OPTION><OPTION value="WHAMMP2">WHAMMP2 (WAS protein homolog associated with actin, golgi membranes and...)</OPTION><OPTION value="ZNF276">ZNF276 (zinc finger protein 276)</OPTION><OPTION value="ZNF423">ZNF423 (zinc finger protein 423)</OPTION><OPTION value="ZNF513">ZNF513 (zinc finger protein 513)</OPTION><OPTION value="ZNF778">ZNF778 (zinc finger protein 778)</OPTION></SELECT><INPUT type="submit" value="Switch"></FORM>';
      document.getElementById('gene_name').innerHTML=sForm;
    }

    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jeegoocontext/jquery.jeegoocontext.min.js"> </SCRIPT>
  <LINK rel="stylesheet" type="text/css" href="lib/jeegoocontext/style.css">
  <LINK rel="stylesheet" type="text/css" href="lib/jQuery/css/cupertino/jquery-ui.custom.css">
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD valign="top" width="424" height="105">
      <IMG src="gfx/GEDI.png" alt="LOVD - Leiden Open Variation Database" width="404" height="100">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">The Genetic Eye Disorder (GEDI) Variation Database</H2>
      <H5 id="gene_name">Bardet-Biedl syndrome 1 (BBS1)&nbsp;<A href="#" onclick="lovd_switchGeneInline(); return false;"><IMG src="gfx/lovd_genes_switch_inline.png" width="23" height="23" alt="Switch gene" title="Switch gene database" align="top"></A></H5>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.3.0 Build 08 [ <A href="status">Current LOVD status</A> ]<BR>
      <A href="users?register"><B>Register as submitter</B></A> | <A href="login"><B>Log in</B></A>
    </TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('gfx/tab_fill.png'); background-repeat : repeat-x;">
      <IMG src="gfx/tab_0F.png" alt="" width="25" height="25" align="left">
      <A href="genes/BBS1"><IMG src="gfx/tab_genes_F.png" alt="BBS1 homepage" id="tab_genes" width="44" height="25" align="left"></A>
      <IMG src="gfx/tab_FB.png" alt="" width="25" height="25" align="left">
      <A href="transcripts/BBS1"><IMG src="gfx/tab_transcripts_B.png" alt="View transcripts" id="tab_transcripts" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="variants/BBS1"><IMG src="gfx/tab_variants_B.png" alt="View variants" id="tab_variants" width="58" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="individuals/BBS1"><IMG src="gfx/tab_individuals_B.png" alt="View individuals" id="tab_individuals" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="diseases?search_genes_=BBS1"><IMG src="gfx/tab_diseases_B.png" alt="View diseases" id="tab_diseases" width="62" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="screenings/BBS1"><IMG src="gfx/tab_screenings_B.png" alt="View screenings" id="tab_screenings" width="78" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="submit"><IMG src="gfx/tab_submit_B.png" alt="Submit new data" id="tab_submit" width="53" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="docs"><IMG src="gfx/tab_docs_B.png" alt="LOVD documentation" id="tab_docs" width="110" height="25" align="left"></A>
      <IMG src="gfx/tab_B0.png" alt="" width="25" height="25" align="left">
    </TD>
  </TR>
</TABLE>

<IMG src="gfx/trans.png" alt="" width="792" height="0">

<!-- Start drop down menu definitions -->
<UL id="menu_tab_genes" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/genes"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genes</A></LI>
  <LI class="icon"><A href="/GEDI/genes/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View the BBS1 gene homepage</A></LI>
  <LI class="icon"><A href="/GEDI/genes/BBS1/graphs"><SPAN class="icon" style="background-image: url(gfx/menu_graphs.png);"></SPAN>View graphs about the BBS1 gene database</A></LI>
</UL>

<UL id="menu_tab_transcripts" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/transcripts"><SPAN class="icon" style="background-image: url(gfx/menu_transcripts.png);"></SPAN>View all transcripts</A></LI>
  <LI class="icon"><A href="/GEDI/transcripts/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_transcripts.png);"></SPAN>View all transcripts of the BBS1 gene</A></LI>
</UL>

<UL id="menu_tab_variants" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/variants"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genomic variants</A></LI>
  <LI class="icon"><A href="/GEDI/variants/in_gene"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all variants affecting transcripts</A></LI>
  <LI class="icon"><A href="/GEDI/variants/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all variants in the BBS1 gene</A></LI>
  <LI class="icon"><A href="/GEDI/view/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>Full data view for the BBS1 gene</A></LI>
</UL>

<UL id="menu_tab_individuals" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/individuals"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all individuals</A></LI>
  <LI class="icon"><A href="/GEDI/individuals/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all individuals screened for BBS1</A></LI>
</UL>

<UL id="menu_tab_diseases" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/diseases"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all diseases</A></LI>
</UL>

<UL id="menu_tab_screenings" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/screenings"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all screenings</A></LI>
  <LI class="icon"><A href="/GEDI/screenings/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all screenings for the BBS1 gene</A></LI>
</UL>

<UL id="menu_tab_submit" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/submit"><SPAN class="icon" style="background-image: url(gfx/plus.png);"></SPAN>Submit new data</A></LI>
</UL>


<SCRIPT type="text/javascript">
  $(function(){
    var aMenuOptions = {
        widthOverflowOffset: 0,
        heightOverflowOffset: 1,
        startLeftOffset: -20,
        event: "mouseover",
        openBelowContext: true,
        autoHide: true,
        delay: 100,
        onSelect: function(e, context){
            if($(this).hasClass("disabled"))
            {
                return false;
            } else {
                window.location = $(this).find("a").attr("href");
                return false;
            }
        }
    };
    $('#tab_genes').jeegoocontext('menu_tab_genes', aMenuOptions);
    $('#tab_transcripts').jeegoocontext('menu_tab_transcripts', aMenuOptions);
    $('#tab_variants').jeegoocontext('menu_tab_variants', aMenuOptions);
    $('#tab_individuals').jeegoocontext('menu_tab_individuals', aMenuOptions);
    $('#tab_diseases').jeegoocontext('menu_tab_diseases', aMenuOptions);
    $('#tab_screenings').jeegoocontext('menu_tab_screenings', aMenuOptions);
    $('#tab_submit').jeegoocontext('menu_tab_submit', aMenuOptions);
  });
</SCRIPT>
<!-- End drop down menu definitions -->



<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD style="padding-top : 10px;">







      <H2 class="LOVD">View gene BBS1</H2>

      <DIV style="text-align : left;">GEDI:The Genetic Eye Disease Panel for Retinal Genes</DIV>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="600" class="data">
        <TR>
          <TH colspan="2" class="S15" valign="top">General information</TH></TR>
        <TR>
          <TH valign="top">Gene&nbsp;symbol</TH>
          <TD>BBS1</TD></TR>
        <TR>
          <TH valign="top">Gene&nbsp;name</TH>
          <TD>Bardet-Biedl syndrome 1</TD></TR>
        <TR>
          <TH valign="top">Chromosome</TH>
          <TD>11</TD></TR>
        <TR>
          <TH valign="top">Chromosomal&nbsp;band</TH>
          <TD>q13</TD></TR>
        <TR>
          <TH valign="top">Imprinted</TH>
          <TD>Unknown</TD></TR>
        <TR>
          <TH valign="top">Genomic&nbsp;reference</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/nuccore/NC_000011.9" target="_blank">NC_000011.9</A></TD></TR>
        <TR>
          <TH valign="top">Transcript&nbsp;reference</TH>
          <TD><A href="transcripts/00059">NM_024649.4</A>, <A href="transcripts/00055">XM_005274126.1</A>, <A href="transcripts/00056">XM_005274127.1</A>, <A href="transcripts/00057">XM_005274128.1</A>, <A href="transcripts/00058">XM_005274129.1</A></TD></TR>
        <TR>
          <TH valign="top">Associated&nbsp;with&nbsp;diseases</TH>
          <TD>-</TD></TR>
        <TR>
          <TH valign="top">Citation&nbsp;reference(s)</TH>
          <TD>http://oculargenomics.meei.harvard.edu/index.php/gdt</TD></TR>
        <TR>
          <TH valign="top">Curators&nbsp;(0)</TH>
          <TD>-</TD></TR>
        <TR>
          <TH valign="top">Total&nbsp;number&nbsp;of&nbsp;public&nbsp;variants&nbsp;reported</TH>
          <TD>0</TD></TR>
        <TR>
          <TH valign="top">Unique&nbsp;public&nbsp;DNA&nbsp;variants&nbsp;reported</TH>
          <TD>0</TD></TR>
        <TR>
          <TH valign="top">Individuals&nbsp;with&nbsp;public&nbsp;variants</TH>
          <TD></TD></TR>
        <TR>
          <TH valign="top">Hidden&nbsp;variants</TH>
          <TD>0</TD></TR>
        <TR>
          <TH valign="top">Notes</TH>
          <TD>GEDI:The Genetic Eye Disease Panel for Retinal Genes</TD></TR>
        <TR>
          <TH valign="top">Date&nbsp;created</TH>
          <TD>November 08, 2013</TD></TR></TABLE>


      <HR>
      <TABLE border="0" cellpadding="0" cellspacing="1" width="600" class="data">
        <TR>
          <TH colspan="2" class="S15" valign="top">Links to other resources</TH></TR>
        <TR>
          <TH valign="top">External&nbsp;URL</TH>
          <TD><A href="http://oculargenomics.meei.harvard.edu/index.php/gdt" target="_blank">http://oculargenomics.meei.harvard.edu/index.php/gdt</A></TD></TR>
        <TR>
          <TH valign="top">HGNC</TH>
          <TD><A href="http://www.genenames.org/data/hgnc_data.php?hgnc_id=966" target="_blank">966</A></TD></TR>
        <TR>
          <TH valign="top">Entrez&nbsp;Gene</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=gene&amp;cmd=Retrieve&amp;dopt=full_report&amp;list_uids=582" target="_blank">582</A></TD></TR>
        <TR>
          <TH valign="top">OMIM&nbsp;-&nbsp;Gene</TH>
          <TD><A href="http://www.omim.org/entry/209901" target="_blank">209901</A></TD></TR>
        <TR>
          <TH valign="top">HGMD</TH>
          <TD><A href="http://www.hgmd.cf.ac.uk/ac/gene.php?gene=BBS1" target="_blank">BBS1</A></TD></TR>
        <TR>
          <TH valign="top">GeneCards</TH>
          <TD><A href="http://www.genecards.org/cgi-bin/carddisp.pl?gene=BBS1" target="_blank">BBS1</A></TD></TR>
        <TR>
          <TH valign="top">GeneTests</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/sites/GeneTests/lab/gene/BBS1" target="_blank">BBS1</A></TD></TR></TABLE>

<BR><BR>

      <H4 class="LOVD">Active transcripts</H4>

      <SCRIPT type="text/javascript" src="inc-js-viewlist.php?nohistory"> </SCRIPT>
      <SCRIPT type="text/javascript" src="inc-js-tooltip.php"> </SCRIPT>
      <FORM action="genes/BBS1" method="get" id="viewlistForm_Transcripts_for_G_VE" style="margin : 0px;" onsubmit="return false;">
        <INPUT type="hidden" name="viewlistid" value="Transcripts_for_G_VE">
        <INPUT type="hidden" name="object" value="Transcript">
        <INPUT type="hidden" name="id" value="0">
        <INPUT type="hidden" name="order" value="variants,DESC">
        <INPUT type="hidden" name="skip[geneid]" value="geneid">
        <INPUT type="hidden" name="search_geneid" value="=&quot;BBS1&quot;">
        <INPUT type="hidden" name="hidenav" value="true">

      <DIV id="viewlistDiv_Transcripts_for_G_VE">
      <DIV id="viewlistLegend_Transcripts_for_G_VE" title="Legend" style="display : none;">
        <H2 class="LOVD">Legend</H2>

        <I class="S11">Please note that a short description of a certain column can be displayed when you move your mouse cursor over the column's header and hold it still. Below, a more detailed description is shown per column.</I><BR><BR>

      </DIV>

      <TABLE border="0" cellpadding="0" cellspacing="1" class="data" id="viewlistTable_Transcripts_for_G_VE">
        <THEAD>
        <TR>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="70" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_id_"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='id_,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_id_" value="" title="ID field should contain..." style="width : 64px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="40" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_chromosome"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='chromosome,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Chr&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_chromosome" value="" title="Chr field should contain..." style="width : 34px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="300" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_name"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='name,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_name" value="" title="Name field should contain..." style="width : 294px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="120" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_id_ncbi"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='id_ncbi,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">NCBI&nbsp;ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_id_ncbi" value="" title="NCBI ID field should contain..." style="width : 114px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="120" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_id_protein_ncbi"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='id_protein_ncbi,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">NCBI&nbsp;Protein&nbsp;ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_id_protein_ncbi" value="" title="NCBI Protein ID field should contain..." style="width : 114px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="ordered">
            <IMG src="gfx/trans.png" alt="" width="70" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_variants"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='variants,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Variants&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_variants" value="" title="Variants field should contain..." style="width : 64px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH></TR></THEAD>
        <TR class="data" id="00055" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/transcripts/00055';">
          <TD><A href="transcripts/00055" class="hide">00055</A></TD>
          <TD>11</TD>
          <TD>transcript variant X1</TD>
          <TD>XM_005274126.1</TD>
          <TD>XP_005274183.1</TD>
          <TD class="ordered">0</TD></TR>
        <TR class="data" id="00056" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/transcripts/00056';">
          <TD><A href="transcripts/00056" class="hide">00056</A></TD>
          <TD>11</TD>
          <TD>transcript variant X2</TD>
          <TD>XM_005274127.1</TD>
          <TD>XP_005274184.1</TD>
          <TD class="ordered">0</TD></TR>
        <TR class="data" id="00057" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/transcripts/00057';">
          <TD><A href="transcripts/00057" class="hide">00057</A></TD>
          <TD>11</TD>
          <TD>transcript variant X3</TD>
          <TD>XM_005274128.1</TD>
          <TD>XP_005274185.1</TD>
          <TD class="ordered">0</TD></TR>
        <TR class="data" id="00058" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/transcripts/00058';">
          <TD><A href="transcripts/00058" class="hide">00058</A></TD>
          <TD>11</TD>
          <TD>transcript variant X4</TD>
          <TD>XM_005274129.1</TD>
          <TD>XP_005274186.1</TD>
          <TD class="ordered">0</TD></TR>
        <TR class="data" id="00059" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/transcripts/00059';">
          <TD><A href="transcripts/00059" class="hide">00059</A></TD>
          <TD>11</TD>
          <TD>Bardet-Biedl syndrome 1</TD>
          <TD>NM_024649.4</TD>
          <TD>NP_078925.3</TD>
          <TD class="ordered">0</TD></TR></TABLE>
      </DIV></FORM><BR>
      <SCRIPT type="text/javascript">
        // This has to be run when the document has finished loading everything, because only then can it get the proper width from IE7 and lower!
        $( function () {lovd_stretchInputs('Transcripts_for_G_VE');});
        check_list['Transcripts_for_G_VE'] = [];
      </SCRIPT>

<BR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="data">
        <TR>
          <TH class="S15">Copyright &amp; disclaimer</TH></TR>
        <TR class="S11">
          <TD>This testing will not detect large genomic structural rearrangements such as deletions, duplications, inversions and insertions.  Variants in non-coding regions which are outside of the splicing regions and not specifically targeted will not be analyzed.  Additionally, genetic variants present in genes not known to be associated with retinal degeneration may not be detected by this testing method.  Research-based testing is available for detecting these types of genetic alterations.</TD></TR></TABLE><BR>

      <DIV style="text-align : left;">The Ocular Genomics Institute (OGI) at Massachusetts Eye and Ear/Harvard Medical School Department of Ophthalmology</DIV>










    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/3.0/" target="_blank">LOVD v.3.0</A> Build 08<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_update_error_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>
<SCRIPT type="text/javascript">
  <!--

function lovd_mapVariants ()
{
    // This function requests the script that will do the actual work.

    // First unbind any onclick handlers on the status image.
    $("#mapping_progress").unbind();

    // Now request the script.
    $.get("ajax/map_variants.php", function (sResponse)
        {
            // The server responded successfully. Let's see what he's saying.
            aResponse = sResponse.split("\t");
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_" + aResponse[1] + (aResponse[1] == "preparing"? ".gif" : ".png"), "title": aResponse[2]});

            if (sResponse.indexOf("Notice") >= 0 || sResponse.indexOf("Warning") >= 0 || sResponse.indexOf("Error") >= 0 || sResponse.indexOf("Fatal") >= 0) {
                // Something went wrong while processing the request, don't try again.
                $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sResponse});
            } else if (aResponse[0] == "1") {
                // More variants to map. Re-call.
                setTimeout("lovd_mapVariants()", 50);
            } else {
                // No more variants to map. But allow the user to try.
                $("#mapping_progress").click(lovd_mapVariants);
            }
        }
    ).fail(function (oObject, sStatus)
        {
            // Something went wrong while contacting the server, don't try again.
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sStatus});
        }
    );
}
$("#mapping_progress").click(lovd_mapVariants);
$("#mapping_progress").attr("Title", "Mapping is temporarily suspended because of network problems on the last attempt. Click to retry.");
  // -->
</SCRIPT>

</BODY>
</HTML>
"""

BBS1_VARIANT_DATABASE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>View transcript variants in BBS1 - The Genetic Eye Disorder (GEDI) Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <META name="author" content="LOVD development team, LUMC, Netherlands">
  <META name="generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <BASE href="http://mseqdr.lumc.edu/GEDI/">
  <LINK rel="stylesheet" type="text/css" href="styles.css">
  <LINK rel="shortcut icon" href="favicon.ico" type="image/x-icon">

  <SCRIPT type="text/javascript" src="inc-js-openwindow.php"> </SCRIPT>
  <SCRIPT type="text/javascript" src="inc-js-toggle-visibility.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery.min.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery-ui.custom.min.js"> </SCRIPT>

  <SCRIPT type="text/javascript">
    <!--

    var sURL = "/GEDI/variants/{{GENE}}";
    function lovd_switchGeneInline () {
      var sForm = '<FORM action="" id="SelectGeneDBInline" method="get" style="margin : 0px;" onsubmit="document.location.href=(sURL.replace(\'{{GENE}}\', $(this).children(\'select\').val())); return false;"><SELECT name="select_db" onchange="$(this).parent().submit();"><OPTION value="ABCA4">ABCA4 (ATP-binding cassette, sub-family A (ABC1), member 4)</OPTION><OPTION value="ABCC6">ABCC6 (ATP-binding cassette, sub-family C (CFTR/MRP), member 6)</OPTION><OPTION value="ABHD12">ABHD12 (abhydrolase domain containing 12)</OPTION><OPTION value="ADAM9">ADAM9 (ADAM metallopeptidase domain 9)</OPTION><OPTION value="ADAMTS18">ADAMTS18 (ADAM metallopeptidase with thrombospondin type 1 motif, 18)</OPTION><OPTION value="AFG3L1P">AFG3L1P (AFG3-like AAA ATPase 1, pseudogene)</OPTION><OPTION value="AHI1">AHI1 (Abelson helper integration site 1)</OPTION><OPTION value="AIP">AIP (aryl hydrocarbon receptor interacting protein)</OPTION><OPTION value="AIPL1">AIPL1 (aryl hydrocarbon receptor interacting protein-like 1)</OPTION><OPTION value="ALMS1">ALMS1 (Alstrom syndrome 1)</OPTION><OPTION value="ANKRD11">ANKRD11 (ankyrin repeat domain 11)</OPTION><OPTION value="ARL13B">ARL13B (ADP-ribosylation factor-like 13B)</OPTION><OPTION value="ARL6">ARL6 (ADP-ribosylation factor-like 6)</OPTION><OPTION value="ARMS2">ARMS2 (age-related maculopathy susceptibility 2)</OPTION><OPTION value="ASIP">ASIP (agouti signaling protein)</OPTION><OPTION value="ATOH7">ATOH7 (atonal homolog 7 (Drosophila))</OPTION><OPTION value="ATXN7">ATXN7 (ataxin 7)</OPTION><OPTION value="B3GALNT2">B3GALNT2 (beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION><OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION><OPTION value="BBS1" selected>BBS1 (Bardet-Biedl syndrome 1)</OPTION><OPTION value="BBS10">BBS10 (Bardet-Biedl syndrome 10)</OPTION><OPTION value="BBS12">BBS12 (Bardet-Biedl syndrome 12)</OPTION><OPTION value="BBS2">BBS2 (Bardet-Biedl syndrome 2)</OPTION><OPTION value="BBS4">BBS4 (Bardet-Biedl syndrome 4)</OPTION><OPTION value="BBS5">BBS5 (Bardet-Biedl syndrome 5)</OPTION><OPTION value="BBS7">BBS7 (Bardet-Biedl syndrome 7)</OPTION><OPTION value="BBS9">BBS9 (Bardet-Biedl syndrome 9)</OPTION><OPTION value="BEST1">BEST1 (bestrophin 1)</OPTION><OPTION value="C10orf105">C10orf105 (chromosome 10 open reading frame 105)</OPTION><OPTION value="C1QTNF5">C1QTNF5 (C1q and tumor necrosis factor related protein 5)</OPTION><OPTION value="C2">C2 (complement component 2)</OPTION><OPTION value="C2orf71">C2orf71 (chromosome 2 open reading frame 71)</OPTION><OPTION value="C3">C3 (complement component 3)</OPTION><OPTION value="C5orf42">C5orf42 (chromosome 5 open reading frame 42)</OPTION><OPTION value="C8orf37">C8orf37 (chromosome 8 open reading frame 37)</OPTION><OPTION value="CA4">CA4 (carbonic anhydrase IV)</OPTION><OPTION value="CABP4">CABP4 (calcium binding protein 4)</OPTION><OPTION value="CACNA1F">CACNA1F (calcium channel, voltage-dependent, L type, alpha 1F subunit)</OPTION><OPTION value="CACNA2D4">CACNA2D4 (calcium channel, voltage-dependent, alpha 2/delta subunit 4)</OPTION><OPTION value="CAPN5">CAPN5 (calpain 5)</OPTION><OPTION value="CC2D2A">CC2D2A (coiled-coil and C2 domain containing 2A)</OPTION><OPTION value="CDH23">CDH23 (cadherin-related 23)</OPTION><OPTION value="CDH3">CDH3 (cadherin 3, type 1, P-cadherin (placental))</OPTION><OPTION value="CDHR1">CDHR1 (cadherin-related family member 1)</OPTION><OPTION value="CDK10">CDK10 (cyclin-dependent kinase 10)</OPTION><OPTION value="CDKL5">CDKL5 (cyclin-dependent kinase-like 5)</OPTION><OPTION value="CENPBD1">CENPBD1 (CENPB DNA-binding domains containing 1)</OPTION><OPTION value="CEP164">CEP164 (centrosomal protein 164kDa)</OPTION><OPTION value="CEP290">CEP290 (centrosomal protein 290kDa)</OPTION><OPTION value="CEP41">CEP41 (centrosomal protein 41kDa)</OPTION><OPTION value="CERKL">CERKL (ceramide kinase-like)</OPTION><OPTION value="CFB">CFB (complement factor B)</OPTION><OPTION value="CFH">CFH (complement factor H)</OPTION><OPTION value="CHM">CHM (choroideremia (Rab escort protein 1))</OPTION><OPTION value="CHMP1A">CHMP1A (charged multivesicular body protein 1A)</OPTION><OPTION value="CIB2">CIB2 (calcium and integrin binding family member 2)</OPTION><OPTION value="CLN3">CLN3 (ceroid-lipofuscinosis, neuronal 3)</OPTION><OPTION value="CLN5">CLN5 (ceroid-lipofuscinosis, neuronal 5)</OPTION><OPTION value="CLN6">CLN6 (ceroid-lipofuscinosis, neuronal 6, late infantile, variant)</OPTION><OPTION value="CLN8">CLN8 (ceroid-lipofuscinosis, neuronal 8 (epilepsy, progressive with me...))</OPTION><OPTION value="CLRN1">CLRN1 (clarin 1)</OPTION><OPTION value="CNGA1">CNGA1 (cyclic nucleotide gated channel alpha 1)</OPTION><OPTION value="CNGA3">CNGA3 (cyclic nucleotide gated channel alpha 3)</OPTION><OPTION value="CNGB1">CNGB1 (cyclic nucleotide gated channel beta 1)</OPTION><OPTION value="CNGB3">CNGB3 (cyclic nucleotide gated channel beta 3)</OPTION><OPTION value="CNNM4">CNNM4 (cyclin M4)</OPTION><OPTION value="COL11A1">COL11A1 (collagen, type XI, alpha 1)</OPTION><OPTION value="COL2A1">COL2A1 (collagen, type II, alpha 1)</OPTION><OPTION value="COL9A1">COL9A1 (collagen, type IX, alpha 1)</OPTION><OPTION value="CPNE7">CPNE7 (copine VII)</OPTION><OPTION value="CRB1">CRB1 (crumbs homolog 1 (Drosophila))</OPTION><OPTION value="CRX">CRX (cone-rod homeobox)</OPTION><OPTION value="CTC1">CTC1 (CTS telomere maintenance complex component 1)</OPTION><OPTION value="CYP1B1">CYP1B1 (cytochrome P450, family 1, subfamily B, polypeptide 1)</OPTION><OPTION value="CYP4V2">CYP4V2 (cytochrome P450, family 4, subfamily V, polypeptide 2)</OPTION><OPTION value="DBNDD1">DBNDD1 (dysbindin (dystrobrevin binding protein 1) domain containing 1)</OPTION><OPTION value="DENND2A">DENND2A (DENN/MADD domain containing 2A)</OPTION><OPTION value="DFNB31">DFNB31 (deafness, autosomal recessive 31)</OPTION><OPTION value="DHDDS">DHDDS (dehydrodolichyl diphosphate synthase)</OPTION><OPTION value="DPEP1">DPEP1 (dipeptidase 1 (renal))</OPTION><OPTION value="EFEMP1">EFEMP1 (EGF containing fibulin-like extracellular matrix protein 1)</OPTION><OPTION value="ELOVL4">ELOVL4 (ELOVL fatty acid elongase 4)</OPTION><OPTION value="ERCC6">ERCC6 (excision repair cross-complementing rodent repair deficiency, co...)</OPTION><OPTION value="ESRRG">ESRRG (estrogen-related receptor gamma)</OPTION><OPTION value="EYS">EYS (eyes shut homolog (Drosophila))</OPTION><OPTION value="FAM161A">FAM161A (family with sequence similarity 161, member A)</OPTION><OPTION value="FAM66B">FAM66B (family with sequence similarity 66, member B)</OPTION><OPTION value="FAM66E">FAM66E (family with sequence similarity 66, member E)</OPTION><OPTION value="FAM78B">FAM78B (family with sequence similarity 78, member B)</OPTION><OPTION value="FANCA">FANCA (Fanconi anemia, complementation group A)</OPTION><OPTION value="FBLN5">FBLN5 (fibulin 5)</OPTION><OPTION value="FBXL17">FBXL17 (F-box and leucine-rich repeat protein 17)</OPTION><OPTION value="FGFR3">FGFR3 (fibroblast growth factor receptor 3)</OPTION><OPTION value="FKRP">FKRP (fukutin related protein)</OPTION><OPTION value="FKTN">FKTN (fukutin)</OPTION><OPTION value="FLVCR1">FLVCR1 (feline leukemia virus subgroup C cellular receptor 1)</OPTION><OPTION value="FSCN2">FSCN2 (fascin homolog 2, actin-bundling protein, retinal (Strongylocen...))</OPTION><OPTION value="FZD4">FZD4 (frizzled family receptor 4)</OPTION><OPTION value="GAS8">GAS8 (growth arrest-specific 8)</OPTION><OPTION value="GIGYF2">GIGYF2 (GRB10 interacting GYF protein 2)</OPTION><OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION><OPTION value="GNAT1">GNAT1 (guanine nucleotide binding protein (G protein), alpha transducin...)</OPTION><OPTION value="GNAT2">GNAT2 (guanine nucleotide binding protein (G protein), alpha transducin...)</OPTION><OPTION value="GNPTG">GNPTG (N-acetylglucosamine-1-phosphate transferase, gamma subunit)</OPTION><OPTION value="GPR143">GPR143 (G protein-coupled receptor 143)</OPTION><OPTION value="GPR179">GPR179 (G protein-coupled receptor 179)</OPTION><OPTION value="GPR98">GPR98 (G protein-coupled receptor 98)</OPTION><OPTION value="GRK1">GRK1 (G protein-coupled receptor kinase 1)</OPTION><OPTION value="GRM6">GRM6 (glutamate receptor, metabotropic 6)</OPTION><OPTION value="GRN">GRN (granulin)</OPTION><OPTION value="GUCA1A">GUCA1A (guanylate cyclase activator 1A (retina))</OPTION><OPTION value="GUCA1B">GUCA1B (guanylate cyclase activator 1B (retina))</OPTION><OPTION value="GUCY2D">GUCY2D (guanylate cyclase 2D, membrane (retina-specific))</OPTION><OPTION value="HARS">HARS (histidyl-tRNA synthetase)</OPTION><OPTION value="HERC2">HERC2 (HECT and RLD domain containing E3 ubiquitin protein ligase 2)</OPTION><OPTION value="HESX1">HESX1 (HESX homeobox 1)</OPTION><OPTION value="HMCN1">HMCN1 (hemicentin 1)</OPTION><OPTION value="HTRA1">HTRA1 (HtrA serine peptidase 1)</OPTION><OPTION value="IDH3B">IDH3B (isocitrate dehydrogenase 3 (NAD+) beta)</OPTION><OPTION value="IFT140">IFT140 (intraflagellar transport 140 homolog (Chlamydomonas))</OPTION><OPTION value="IFT80">IFT80 (intraflagellar transport 80 homolog (Chlamydomonas))</OPTION><OPTION value="IMPDH1">IMPDH1 (IMP (inosine 5\'-monophosphate) dehydrogenase 1)</OPTION><OPTION value="IMPG2">IMPG2 (interphotoreceptor matrix proteoglycan 2)</OPTION><OPTION value="INPP5E">INPP5E (inositol polyphosphate-5-phosphatase, 72 kDa)</OPTION><OPTION value="INVS">INVS (inversin)</OPTION><OPTION value="IQCB1">IQCB1 (IQ motif containing B1)</OPTION><OPTION value="IRF4">IRF4 (interferon regulatory factor 4)</OPTION><OPTION value="ISPD">ISPD (isoprenoid synthase domain containing)</OPTION><OPTION value="JAG1">JAG1 (jagged 1)</OPTION><OPTION value="KCNJ13">KCNJ13 (potassium inwardly-rectifying channel, subfamily J, member 13)</OPTION><OPTION value="KCNV2">KCNV2 (potassium channel, subfamily V, member 2)</OPTION><OPTION value="KCTD7">KCTD7 (potassium channel tetramerization domain containing 7)</OPTION><OPTION value="KIF11">KIF11 (kinesin family member 11)</OPTION><OPTION value="KLHL7">KLHL7 (kelch-like family member 7)</OPTION><OPTION value="LARGE">LARGE (like-glycosyltransferase)</OPTION><OPTION value="LCA5">LCA5 (Leber congenital amaurosis 5)</OPTION><OPTION value="LCAT">LCAT (lecithin-cholesterol acyltransferase)</OPTION><OPTION value="LRAT">LRAT (lecithin retinol acyltransferase (phosphatidylcholine--retinol O...))</OPTION><OPTION value="LRIT3">LRIT3 (leucine-rich repeat, immunoglobulin-like and transmembrane domai...)</OPTION><OPTION value="LRP1B">LRP1B (low density lipoprotein receptor-related protein 1B)</OPTION><OPTION value="LRP5">LRP5 (low density lipoprotein receptor-related protein 5)</OPTION><OPTION value="LZTFL1">LZTFL1 (leucine zipper transcription factor-like 1)</OPTION><OPTION value="MAK">MAK (male germ cell-associated kinase)</OPTION><OPTION value="MC1R">MC1R (melanocortin 1 receptor (alpha melanocyte stimulating hormone re...))</OPTION><OPTION value="MERTK">MERTK (c-mer proto-oncogene tyrosine kinase)</OPTION><OPTION value="MFN2">MFN2 (mitofusin 2)</OPTION><OPTION value="MFRP">MFRP (membrane frizzled-related protein)</OPTION><OPTION value="MFSD8">MFSD8 (major facilitator superfamily domain containing 8)</OPTION><OPTION value="MKKS">MKKS (McKusick-Kaufman syndrome)</OPTION><OPTION value="MKS1">MKS1 (Meckel syndrome, type 1)</OPTION><OPTION value="MSH4">MSH4 (mutS homolog 4)</OPTION><OPTION value="MTAP">MTAP (methylthioadenosine phosphorylase)</OPTION><OPTION value="MTTP">MTTP (microsomal triglyceride transfer protein)</OPTION><OPTION value="MYH9">MYH9 (myosin, heavy chain 9, non-muscle)</OPTION><OPTION value="MYO7A">MYO7A (myosin VIIA)</OPTION><OPTION value="MYPN">MYPN (myopalladin)</OPTION><OPTION value="NBAS">NBAS (neuroblastoma amplified sequence)</OPTION><OPTION value="NDP">NDP (Norrie disease (pseudoglioma))</OPTION><OPTION value="NEK4">NEK4 (NIMA-related kinase 4)</OPTION><OPTION value="NEK8">NEK8 (NIMA-related kinase 8)</OPTION><OPTION value="NMNAT1">NMNAT1 (nicotinamide nucleotide adenylyltransferase 1)</OPTION><OPTION value="NPHP1">NPHP1 (nephronophthisis 1 (juvenile))</OPTION><OPTION value="NPHP3">NPHP3 (nephronophthisis 3 (adolescent))</OPTION><OPTION value="NPHP4">NPHP4 (nephronophthisis 4)</OPTION><OPTION value="NPLOC4">NPLOC4 (nuclear protein localization 4 homolog (S. cerevisiae))</OPTION><OPTION value="NR2E3">NR2E3 (nuclear receptor subfamily 2, group E, member 3)</OPTION><OPTION value="NRL">NRL (neural retina leucine zipper)</OPTION><OPTION value="NUB1">NUB1 (negative regulator of ubiquitin-like proteins 1)</OPTION><OPTION value="NYX">NYX (nyctalopin)</OPTION><OPTION value="OAT">OAT (ornithine aminotransferase)</OPTION><OPTION value="OCA2">OCA2 (oculocutaneous albinism II)</OPTION><OPTION value="OFD1">OFD1 (oral-facial-digital syndrome 1)</OPTION><OPTION value="OPA1">OPA1 (optic atrophy 1 (autosomal dominant))</OPTION><OPTION value="OPA1-AS1">OPA1-AS1 (OPA1 antisense RNA 1)</OPTION><OPTION value="OPA3">OPA3 (optic atrophy 3 (autosomal recessive, with chorea and spastic pa...))</OPTION><OPTION value="OPN1LW">OPN1LW (opsin 1 (cone pigments), long-wave-sensitive)</OPTION><OPTION value="OPN1MW">OPN1MW (opsin 1 (cone pigments), medium-wave-sensitive)</OPTION><OPTION value="OPN1SW">OPN1SW (opsin 1 (cone pigments), short-wave-sensitive)</OPTION><OPTION value="OTX2">OTX2 (orthodenticle homeobox 2)</OPTION><OPTION value="PANK2">PANK2 (pantothenate kinase 2)</OPTION><OPTION value="PAX2">PAX2 (paired box 2)</OPTION><OPTION value="PAX6">PAX6 (paired box 6)</OPTION><OPTION value="PCDH15">PCDH15 (protocadherin-related 15)</OPTION><OPTION value="PDE6A">PDE6A (phosphodiesterase 6A, cGMP-specific, rod, alpha)</OPTION><OPTION value="PDE6B">PDE6B (phosphodiesterase 6B, cGMP-specific, rod, beta)</OPTION><OPTION value="PDE6C">PDE6C (phosphodiesterase 6C, cGMP-specific, cone, alpha prime)</OPTION><OPTION value="PDE6G">PDE6G (phosphodiesterase 6G, cGMP-specific, rod, gamma)</OPTION><OPTION value="PDE6H">PDE6H (phosphodiesterase 6H, cGMP-specific, cone, gamma)</OPTION><OPTION value="PDZD7">PDZD7 (PDZ domain containing 7)</OPTION><OPTION value="PEX1">PEX1 (peroxisomal biogenesis factor 1)</OPTION><OPTION value="PEX10">PEX10 (peroxisomal biogenesis factor 10)</OPTION><OPTION value="PEX14">PEX14 (peroxisomal biogenesis factor 14)</OPTION><OPTION value="PEX16">PEX16 (peroxisomal biogenesis factor 16)</OPTION><OPTION value="PEX19">PEX19 (peroxisomal biogenesis factor 19)</OPTION><OPTION value="PEX2">PEX2 (peroxisomal biogenesis factor 2)</OPTION><OPTION value="PEX5">PEX5 (peroxisomal biogenesis factor 5)</OPTION><OPTION value="PEX6">PEX6 (peroxisomal biogenesis factor 6)</OPTION><OPTION value="PEX7">PEX7 (peroxisomal biogenesis factor 7)</OPTION><OPTION value="PGK1">PGK1 (phosphoglycerate kinase 1)</OPTION><OPTION value="PHYH">PHYH (phytanoyl-CoA 2-hydroxylase)</OPTION><OPTION value="PITPNM3">PITPNM3 (PITPNM family member 3)</OPTION><OPTION value="PLA2G5">PLA2G5 (phospholipase A2, group V)</OPTION><OPTION value="POMGNT1">POMGNT1 (protein O-linked mannose N-acetylglucosaminyltransferase 1 (b...))</OPTION><OPTION value="POMT1">POMT1 (protein-O-mannosyltransferase 1)</OPTION><OPTION value="POMT2">POMT2 (protein-O-mannosyltransferase 2)</OPTION><OPTION value="PPT1">PPT1 (palmitoyl-protein thioesterase 1)</OPTION><OPTION value="PRCD">PRCD (progressive rod-cone degeneration)</OPTION><OPTION value="PRDM7">PRDM7 (PR domain containing 7)</OPTION><OPTION value="PROM1">PROM1 (prominin 1)</OPTION><OPTION value="PRPF3">PRPF3 (pre-mRNA processing factor 3)</OPTION><OPTION value="PRPF31">PRPF31 (pre-mRNA processing factor 31)</OPTION><OPTION value="PRPF6">PRPF6 (pre-mRNA processing factor 6)</OPTION><OPTION value="PRPF8">PRPF8 (pre-mRNA processing factor 8)</OPTION><OPTION value="PRPH2">PRPH2 (peripherin 2 (retinal degeneration, slow))</OPTION><OPTION value="RAB28">RAB28 (RAB28, member RAS oncogene family)</OPTION><OPTION value="RAX2">RAX2 (retina and anterior neural fold homeobox 2)</OPTION><OPTION value="RB1">RB1 (retinoblastoma 1)</OPTION><OPTION value="RBP3">RBP3 (retinol binding protein 3, interstitial)</OPTION><OPTION value="RBP4">RBP4 (retinol binding protein 4, plasma)</OPTION><OPTION value="RD3">RD3 (retinal degeneration 3)</OPTION><OPTION value="RDH12">RDH12 (retinol dehydrogenase 12 (all-trans/9-cis/11-cis))</OPTION><OPTION value="RDH5">RDH5 (retinol dehydrogenase 5 (11-cis/9-cis))</OPTION><OPTION value="RFTN1">RFTN1 (raftlin, lipid raft linker 1)</OPTION><OPTION value="RGR">RGR (retinal G protein coupled receptor)</OPTION><OPTION value="RGS9">RGS9 (regulator of G-protein signaling 9)</OPTION><OPTION value="RGS9BP">RGS9BP (regulator of G protein signaling 9 binding protein)</OPTION><OPTION value="RHO">RHO (rhodopsin)</OPTION><OPTION value="RIMS1">RIMS1 (regulating synaptic membrane exocytosis 1)</OPTION><OPTION value="RLBP1">RLBP1 (retinaldehyde binding protein 1)</OPTION><OPTION value="ROM1">ROM1 (retinal outer segment membrane protein 1)</OPTION><OPTION value="RP1">RP1 (retinitis pigmentosa 1 (autosomal dominant))</OPTION><OPTION value="RP1L1">RP1L1 (retinitis pigmentosa 1-like 1)</OPTION><OPTION value="RP2">RP2 (retinitis pigmentosa 2 (X-linked recessive))</OPTION><OPTION value="RP9">RP9 (retinitis pigmentosa 9 (autosomal dominant))</OPTION><OPTION value="RPE65">RPE65 (retinal pigment epithelium-specific protein 65kDa)</OPTION><OPTION value="RPGR">RPGR (retinitis pigmentosa GTPase regulator)</OPTION><OPTION value="RPGRIP1">RPGRIP1 (retinitis pigmentosa GTPase regulator interacting protein 1)</OPTION><OPTION value="RPGRIP1L">RPGRIP1L (RPGRIP1-like)</OPTION><OPTION value="RS1">RS1 (retinoschisin 1)</OPTION><OPTION value="SAG">SAG (S-antigen; retina and pineal gland (arrestin))</OPTION><OPTION value="SCFD2">SCFD2 (sec1 family domain containing 2)</OPTION><OPTION value="SDCCAG8">SDCCAG8 (serologically defined colon cancer antigen 8)</OPTION><OPTION value="SEMA4A">SEMA4A (sema domain, immunoglobulin domain (Ig), transmembrane domain ...)</OPTION><OPTION value="SLC12A4">SLC12A4 (solute carrier family 12 (potassium/chloride transporter), mem...)</OPTION><OPTION value="SLC24A1">SLC24A1 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC24A4">SLC24A4 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC24A5">SLC24A5 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC45A2">SLC45A2 (solute carrier family 45, member 2)</OPTION><OPTION value="SNRNP200">SNRNP200 (small nuclear ribonucleoprotein 200kDa (U5))</OPTION><OPTION value="SOX2">SOX2 (SRY (sex determining region Y)-box 2)</OPTION><OPTION value="SOX2-OT">SOX2-OT (SOX2 overlapping transcript (non-protein coding))</OPTION><OPTION value="SPATA2L">SPATA2L (spermatogenesis associated 2-like)</OPTION><OPTION value="SPATA7">SPATA7 (spermatogenesis associated 7)</OPTION><OPTION value="SPG7">SPG7 (spastic paraplegia 7 (pure and complicated autosomal recessive))</OPTION><OPTION value="SPIRE2">SPIRE2 (spire-type actin nucleation factor 2)</OPTION><OPTION value="TEAD1">TEAD1 (TEA domain family member 1 (SV40 transcriptional enhancer factor))</OPTION><OPTION value="TIMM8A">TIMM8A (translocase of inner mitochondrial membrane 8 homolog A (yeast))</OPTION><OPTION value="TIMP3">TIMP3 (TIMP metallopeptidase inhibitor 3)</OPTION><OPTION value="TLR3">TLR3 (toll-like receptor 3)</OPTION><OPTION value="TLR4">TLR4 (toll-like receptor 4)</OPTION><OPTION value="TMEM126A">TMEM126A (transmembrane protein 126A)</OPTION><OPTION value="TMEM231">TMEM231 (transmembrane protein 231)</OPTION><OPTION value="TMEM237">TMEM237 (transmembrane protein 237)</OPTION><OPTION value="TMEM5">TMEM5 (transmembrane protein 5)</OPTION><OPTION value="TMEM67">TMEM67 (transmembrane protein 67)</OPTION><OPTION value="TOPORS">TOPORS (topoisomerase I binding, arginine/serine-rich, E3 ubiquitin pro...)</OPTION><OPTION value="TPCN2">TPCN2 (two pore segment channel 2)</OPTION><OPTION value="TPP1">TPP1 (tripeptidyl peptidase I)</OPTION><OPTION value="TREX1">TREX1 (three prime repair exonuclease 1)</OPTION><OPTION value="TRIM32">TRIM32 (tripartite motif containing 32)</OPTION><OPTION value="TRPM1">TRPM1 (transient receptor potential cation channel, subfamily M, member 1)</OPTION><OPTION value="TSHR">TSHR (thyroid stimulating hormone receptor)</OPTION><OPTION value="TSPAN12">TSPAN12 (tetraspanin 12)</OPTION><OPTION value="TTC21B">TTC21B (tetratricopeptide repeat domain 21B)</OPTION><OPTION value="TTC3">TTC3 (tetratricopeptide repeat domain 3)</OPTION><OPTION value="TTC8">TTC8 (tetratricopeptide repeat domain 8)</OPTION><OPTION value="TTPA">TTPA (tocopherol (alpha) transfer protein)</OPTION><OPTION value="TTR">TTR (transthyretin)</OPTION><OPTION value="TUBGCP6">TUBGCP6 (tubulin, gamma complex associated protein 6)</OPTION><OPTION value="TULP1">TULP1 (tubby like protein 1)</OPTION><OPTION value="TWIST1">TWIST1 (twist family bHLH transcription factor 1)</OPTION><OPTION value="TYR">TYR (tyrosinase)</OPTION><OPTION value="TYRP1">TYRP1 (tyrosinase-related protein 1)</OPTION><OPTION value="UCHL1">UCHL1 (ubiquitin carboxyl-terminal esterase L1 (ubiquitin thiolesterase))</OPTION><OPTION value="UNC119">UNC119 (unc-119 homolog (C. elegans))</OPTION><OPTION value="USH1C">USH1C (Usher syndrome 1C (autosomal recessive, severe))</OPTION><OPTION value="USH1G">USH1G (Usher syndrome 1G (autosomal recessive))</OPTION><OPTION value="USH2A">USH2A (Usher syndrome 2A (autosomal recessive, mild))</OPTION><OPTION value="VCAN">VCAN (versican)</OPTION><OPTION value="VPS13B">VPS13B (vacuolar protein sorting 13 homolog B (yeast))</OPTION><OPTION value="WDPCP">WDPCP (WD repeat containing planar cell polarity effector)</OPTION><OPTION value="WDR19">WDR19 (WD repeat domain 19)</OPTION><OPTION value="WFS1">WFS1 (Wolfram syndrome 1 (wolframin))</OPTION><OPTION value="WHAMMP2">WHAMMP2 (WAS protein homolog associated with actin, golgi membranes and...)</OPTION><OPTION value="ZNF276">ZNF276 (zinc finger protein 276)</OPTION><OPTION value="ZNF423">ZNF423 (zinc finger protein 423)</OPTION><OPTION value="ZNF513">ZNF513 (zinc finger protein 513)</OPTION><OPTION value="ZNF778">ZNF778 (zinc finger protein 778)</OPTION></SELECT><INPUT type="submit" value="Switch"></FORM>';
      document.getElementById('gene_name').innerHTML=sForm;
    }

    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jeegoocontext/jquery.jeegoocontext.min.js"> </SCRIPT>
  <LINK rel="stylesheet" type="text/css" href="lib/jeegoocontext/style.css">
  <LINK rel="stylesheet" type="text/css" href="lib/jQuery/css/cupertino/jquery-ui.custom.css">
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD valign="top" width="424" height="105">
      <IMG src="gfx/GEDI.png" alt="LOVD - Leiden Open Variation Database" width="404" height="100">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">The Genetic Eye Disorder (GEDI) Variation Database</H2>
      <H5 id="gene_name">Bardet-Biedl syndrome 1 (BBS1)&nbsp;<A href="#" onclick="lovd_switchGeneInline(); return false;"><IMG src="gfx/lovd_genes_switch_inline.png" width="23" height="23" alt="Switch gene" title="Switch gene database" align="top"></A></H5>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.3.0 Build 08 [ <A href="status">Current LOVD status</A> ]<BR>
      <A href="users?register"><B>Register as submitter</B></A> | <A href="login"><B>Log in</B></A>
    </TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('gfx/tab_fill.png'); background-repeat : repeat-x;">
      <IMG src="gfx/tab_0B.png" alt="" width="25" height="25" align="left">
      <A href="genes/BBS1"><IMG src="gfx/tab_genes_B.png" alt="BBS1 homepage" id="tab_genes" width="44" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="transcripts/BBS1"><IMG src="gfx/tab_transcripts_B.png" alt="View transcripts" id="tab_transcripts" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BF.png" alt="" width="25" height="25" align="left">
      <A href="variants/BBS1"><IMG src="gfx/tab_variants_F.png" alt="View variants" id="tab_variants" width="58" height="25" align="left"></A>
      <IMG src="gfx/tab_FB.png" alt="" width="25" height="25" align="left">
      <A href="individuals/BBS1"><IMG src="gfx/tab_individuals_B.png" alt="View individuals" id="tab_individuals" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="diseases?search_genes_=BBS1"><IMG src="gfx/tab_diseases_B.png" alt="View diseases" id="tab_diseases" width="62" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="screenings/BBS1"><IMG src="gfx/tab_screenings_B.png" alt="View screenings" id="tab_screenings" width="78" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="submit"><IMG src="gfx/tab_submit_B.png" alt="Submit new data" id="tab_submit" width="53" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="docs"><IMG src="gfx/tab_docs_B.png" alt="LOVD documentation" id="tab_docs" width="110" height="25" align="left"></A>
      <IMG src="gfx/tab_B0.png" alt="" width="25" height="25" align="left">
    </TD>
  </TR>
</TABLE>

<IMG src="gfx/trans.png" alt="" width="792" height="0">

<!-- Start drop down menu definitions -->
<UL id="menu_tab_genes" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/genes"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genes</A></LI>
  <LI class="icon"><A href="/GEDI/genes/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View the BBS1 gene homepage</A></LI>
  <LI class="icon"><A href="/GEDI/genes/BBS1/graphs"><SPAN class="icon" style="background-image: url(gfx/menu_graphs.png);"></SPAN>View graphs about the BBS1 gene database</A></LI>
</UL>

<UL id="menu_tab_transcripts" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/transcripts"><SPAN class="icon" style="background-image: url(gfx/menu_transcripts.png);"></SPAN>View all transcripts</A></LI>
  <LI class="icon"><A href="/GEDI/transcripts/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_transcripts.png);"></SPAN>View all transcripts of the BBS1 gene</A></LI>
</UL>

<UL id="menu_tab_variants" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/variants"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genomic variants</A></LI>
  <LI class="icon"><A href="/GEDI/variants/in_gene"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all variants affecting transcripts</A></LI>
  <LI class="icon"><A href="/GEDI/variants/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all variants in the BBS1 gene</A></LI>
  <LI class="icon"><A href="/GEDI/view/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>Full data view for the BBS1 gene</A></LI>
</UL>

<UL id="menu_tab_individuals" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/individuals"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all individuals</A></LI>
  <LI class="icon"><A href="/GEDI/individuals/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all individuals screened for BBS1</A></LI>
</UL>

<UL id="menu_tab_diseases" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/diseases"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all diseases</A></LI>
</UL>

<UL id="menu_tab_screenings" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/screenings"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all screenings</A></LI>
  <LI class="icon"><A href="/GEDI/screenings/BBS1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all screenings for the BBS1 gene</A></LI>
</UL>

<UL id="menu_tab_submit" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/submit"><SPAN class="icon" style="background-image: url(gfx/plus.png);"></SPAN>Submit new data</A></LI>
</UL>


<SCRIPT type="text/javascript">
  $(function(){
    var aMenuOptions = {
        widthOverflowOffset: 0,
        heightOverflowOffset: 1,
        startLeftOffset: -20,
        event: "mouseover",
        openBelowContext: true,
        autoHide: true,
        delay: 100,
        onSelect: function(e, context){
            if($(this).hasClass("disabled"))
            {
                return false;
            } else {
                window.location = $(this).find("a").attr("href");
                return false;
            }
        }
    };
    $('#tab_genes').jeegoocontext('menu_tab_genes', aMenuOptions);
    $('#tab_transcripts').jeegoocontext('menu_tab_transcripts', aMenuOptions);
    $('#tab_variants').jeegoocontext('menu_tab_variants', aMenuOptions);
    $('#tab_individuals').jeegoocontext('menu_tab_individuals', aMenuOptions);
    $('#tab_diseases').jeegoocontext('menu_tab_diseases', aMenuOptions);
    $('#tab_screenings').jeegoocontext('menu_tab_screenings', aMenuOptions);
    $('#tab_submit').jeegoocontext('menu_tab_submit', aMenuOptions);
  });
</SCRIPT>
<!-- End drop down menu definitions -->



<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD style="padding-top : 10px;">







      <H2 class="LOVD">View transcript variants in BBS1</H2>

      <DIV style="text-align : left;">GEDI:The Genetic Eye Disease Panel for Retinal Genes</DIV>

      <TABLE border="0" cellpadding="2" cellspacing="0" width="100%" class="info">
        <TR>
          <TD valign="top" align="center" width="40"><IMG src="gfx/lovd_information.png" alt="Information" title="Information" width="32" height="32" style="margin : 4px;"></TD>
          <TD valign="middle">No transcripts or variants found for this gene.</TD></TR></TABLE><BR>

      <DIV style="text-align : left;">The Ocular Genomics Institute (OGI) at Massachusetts Eye and Ear/Harvard Medical School Department of Ophthalmology</DIV>










    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/3.0/" target="_blank">LOVD v.3.0</A> Build 08<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_update_error_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>
<SCRIPT type="text/javascript">
  <!--

function lovd_mapVariants ()
{
    // This function requests the script that will do the actual work.

    // First unbind any onclick handlers on the status image.
    $("#mapping_progress").unbind();

    // Now request the script.
    $.get("ajax/map_variants.php", function (sResponse)
        {
            // The server responded successfully. Let's see what he's saying.
            aResponse = sResponse.split("\t");
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_" + aResponse[1] + (aResponse[1] == "preparing"? ".gif" : ".png"), "title": aResponse[2]});

            if (sResponse.indexOf("Notice") >= 0 || sResponse.indexOf("Warning") >= 0 || sResponse.indexOf("Error") >= 0 || sResponse.indexOf("Fatal") >= 0) {
                // Something went wrong while processing the request, don't try again.
                $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sResponse});
            } else if (aResponse[0] == "1") {
                // More variants to map. Re-call.
                setTimeout("lovd_mapVariants()", 50);
            } else {
                // No more variants to map. But allow the user to try.
                $("#mapping_progress").click(lovd_mapVariants);
            }
        }
    ).fail(function (oObject, sStatus)
        {
            // Something went wrong while contacting the server, don't try again.
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sStatus});
        }
    );
}
$("#mapping_progress").click(lovd_mapVariants);
$("#mapping_progress").attr("Title", "Mapping is temporarily suspended because of network problems on the last attempt. Click to retry.");
  // -->
</SCRIPT>

</BODY>
</HTML>
"""

BBS1_TABLE_DATA = []

CTC1_GENE_HOMEPAGE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>View gene CTC1 - The Genetic Eye Disorder (GEDI) Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <META name="author" content="LOVD development team, LUMC, Netherlands">
  <META name="generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <BASE href="http://mseqdr.lumc.edu/GEDI/">
  <LINK rel="stylesheet" type="text/css" href="styles.css">
  <LINK rel="shortcut icon" href="favicon.ico" type="image/x-icon">

  <SCRIPT type="text/javascript" src="inc-js-openwindow.php"> </SCRIPT>
  <SCRIPT type="text/javascript" src="inc-js-toggle-visibility.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery.min.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery-ui.custom.min.js"> </SCRIPT>

  <SCRIPT type="text/javascript">
    <!--

    var sURL = "/GEDI/genes/{{GENE}}";
    function lovd_switchGeneInline () {
      var sForm = '<FORM action="" id="SelectGeneDBInline" method="get" style="margin : 0px;" onsubmit="document.location.href=(sURL.replace(\'{{GENE}}\', $(this).children(\'select\').val())); return false;"><SELECT name="select_db" onchange="$(this).parent().submit();"><OPTION value="ABCA4">ABCA4 (ATP-binding cassette, sub-family A (ABC1), member 4)</OPTION><OPTION value="ABCC6">ABCC6 (ATP-binding cassette, sub-family C (CFTR/MRP), member 6)</OPTION><OPTION value="ABHD12">ABHD12 (abhydrolase domain containing 12)</OPTION><OPTION value="ADAM9">ADAM9 (ADAM metallopeptidase domain 9)</OPTION><OPTION value="ADAMTS18">ADAMTS18 (ADAM metallopeptidase with thrombospondin type 1 motif, 18)</OPTION><OPTION value="AFG3L1P">AFG3L1P (AFG3-like AAA ATPase 1, pseudogene)</OPTION><OPTION value="AHI1">AHI1 (Abelson helper integration site 1)</OPTION><OPTION value="AIP">AIP (aryl hydrocarbon receptor interacting protein)</OPTION><OPTION value="AIPL1">AIPL1 (aryl hydrocarbon receptor interacting protein-like 1)</OPTION><OPTION value="ALMS1">ALMS1 (Alstrom syndrome 1)</OPTION><OPTION value="ANKRD11">ANKRD11 (ankyrin repeat domain 11)</OPTION><OPTION value="ARL13B">ARL13B (ADP-ribosylation factor-like 13B)</OPTION><OPTION value="ARL6">ARL6 (ADP-ribosylation factor-like 6)</OPTION><OPTION value="ARMS2">ARMS2 (age-related maculopathy susceptibility 2)</OPTION><OPTION value="ASIP">ASIP (agouti signaling protein)</OPTION><OPTION value="ATOH7">ATOH7 (atonal homolog 7 (Drosophila))</OPTION><OPTION value="ATXN7">ATXN7 (ataxin 7)</OPTION><OPTION value="B3GALNT2">B3GALNT2 (beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION><OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION><OPTION value="BBS1">BBS1 (Bardet-Biedl syndrome 1)</OPTION><OPTION value="BBS10">BBS10 (Bardet-Biedl syndrome 10)</OPTION><OPTION value="BBS12">BBS12 (Bardet-Biedl syndrome 12)</OPTION><OPTION value="BBS2">BBS2 (Bardet-Biedl syndrome 2)</OPTION><OPTION value="BBS4">BBS4 (Bardet-Biedl syndrome 4)</OPTION><OPTION value="BBS5">BBS5 (Bardet-Biedl syndrome 5)</OPTION><OPTION value="BBS7">BBS7 (Bardet-Biedl syndrome 7)</OPTION><OPTION value="BBS9">BBS9 (Bardet-Biedl syndrome 9)</OPTION><OPTION value="BEST1">BEST1 (bestrophin 1)</OPTION><OPTION value="C10orf105">C10orf105 (chromosome 10 open reading frame 105)</OPTION><OPTION value="C1QTNF5">C1QTNF5 (C1q and tumor necrosis factor related protein 5)</OPTION><OPTION value="C2">C2 (complement component 2)</OPTION><OPTION value="C2orf71">C2orf71 (chromosome 2 open reading frame 71)</OPTION><OPTION value="C3">C3 (complement component 3)</OPTION><OPTION value="C5orf42">C5orf42 (chromosome 5 open reading frame 42)</OPTION><OPTION value="C8orf37">C8orf37 (chromosome 8 open reading frame 37)</OPTION><OPTION value="CA4">CA4 (carbonic anhydrase IV)</OPTION><OPTION value="CABP4">CABP4 (calcium binding protein 4)</OPTION><OPTION value="CACNA1F">CACNA1F (calcium channel, voltage-dependent, L type, alpha 1F subunit)</OPTION><OPTION value="CACNA2D4">CACNA2D4 (calcium channel, voltage-dependent, alpha 2/delta subunit 4)</OPTION><OPTION value="CAPN5">CAPN5 (calpain 5)</OPTION><OPTION value="CC2D2A">CC2D2A (coiled-coil and C2 domain containing 2A)</OPTION><OPTION value="CDH23">CDH23 (cadherin-related 23)</OPTION><OPTION value="CDH3">CDH3 (cadherin 3, type 1, P-cadherin (placental))</OPTION><OPTION value="CDHR1">CDHR1 (cadherin-related family member 1)</OPTION><OPTION value="CDK10">CDK10 (cyclin-dependent kinase 10)</OPTION><OPTION value="CDKL5">CDKL5 (cyclin-dependent kinase-like 5)</OPTION><OPTION value="CENPBD1">CENPBD1 (CENPB DNA-binding domains containing 1)</OPTION><OPTION value="CEP164">CEP164 (centrosomal protein 164kDa)</OPTION><OPTION value="CEP290">CEP290 (centrosomal protein 290kDa)</OPTION><OPTION value="CEP41">CEP41 (centrosomal protein 41kDa)</OPTION><OPTION value="CERKL">CERKL (ceramide kinase-like)</OPTION><OPTION value="CFB">CFB (complement factor B)</OPTION><OPTION value="CFH">CFH (complement factor H)</OPTION><OPTION value="CHM">CHM (choroideremia (Rab escort protein 1))</OPTION><OPTION value="CHMP1A">CHMP1A (charged multivesicular body protein 1A)</OPTION><OPTION value="CIB2">CIB2 (calcium and integrin binding family member 2)</OPTION><OPTION value="CLN3">CLN3 (ceroid-lipofuscinosis, neuronal 3)</OPTION><OPTION value="CLN5">CLN5 (ceroid-lipofuscinosis, neuronal 5)</OPTION><OPTION value="CLN6">CLN6 (ceroid-lipofuscinosis, neuronal 6, late infantile, variant)</OPTION><OPTION value="CLN8">CLN8 (ceroid-lipofuscinosis, neuronal 8 (epilepsy, progressive with me...))</OPTION><OPTION value="CLRN1">CLRN1 (clarin 1)</OPTION><OPTION value="CNGA1">CNGA1 (cyclic nucleotide gated channel alpha 1)</OPTION><OPTION value="CNGA3">CNGA3 (cyclic nucleotide gated channel alpha 3)</OPTION><OPTION value="CNGB1">CNGB1 (cyclic nucleotide gated channel beta 1)</OPTION><OPTION value="CNGB3">CNGB3 (cyclic nucleotide gated channel beta 3)</OPTION><OPTION value="CNNM4">CNNM4 (cyclin M4)</OPTION><OPTION value="COL11A1">COL11A1 (collagen, type XI, alpha 1)</OPTION><OPTION value="COL2A1">COL2A1 (collagen, type II, alpha 1)</OPTION><OPTION value="COL9A1">COL9A1 (collagen, type IX, alpha 1)</OPTION><OPTION value="CPNE7">CPNE7 (copine VII)</OPTION><OPTION value="CRB1">CRB1 (crumbs homolog 1 (Drosophila))</OPTION><OPTION value="CRX">CRX (cone-rod homeobox)</OPTION><OPTION value="CTC1" selected>CTC1 (CTS telomere maintenance complex component 1)</OPTION><OPTION value="CYP1B1">CYP1B1 (cytochrome P450, family 1, subfamily B, polypeptide 1)</OPTION><OPTION value="CYP4V2">CYP4V2 (cytochrome P450, family 4, subfamily V, polypeptide 2)</OPTION><OPTION value="DBNDD1">DBNDD1 (dysbindin (dystrobrevin binding protein 1) domain containing 1)</OPTION><OPTION value="DENND2A">DENND2A (DENN/MADD domain containing 2A)</OPTION><OPTION value="DFNB31">DFNB31 (deafness, autosomal recessive 31)</OPTION><OPTION value="DHDDS">DHDDS (dehydrodolichyl diphosphate synthase)</OPTION><OPTION value="DPEP1">DPEP1 (dipeptidase 1 (renal))</OPTION><OPTION value="EFEMP1">EFEMP1 (EGF containing fibulin-like extracellular matrix protein 1)</OPTION><OPTION value="ELOVL4">ELOVL4 (ELOVL fatty acid elongase 4)</OPTION><OPTION value="ERCC6">ERCC6 (excision repair cross-complementing rodent repair deficiency, co...)</OPTION><OPTION value="ESRRG">ESRRG (estrogen-related receptor gamma)</OPTION><OPTION value="EYS">EYS (eyes shut homolog (Drosophila))</OPTION><OPTION value="FAM161A">FAM161A (family with sequence similarity 161, member A)</OPTION><OPTION value="FAM66B">FAM66B (family with sequence similarity 66, member B)</OPTION><OPTION value="FAM66E">FAM66E (family with sequence similarity 66, member E)</OPTION><OPTION value="FAM78B">FAM78B (family with sequence similarity 78, member B)</OPTION><OPTION value="FANCA">FANCA (Fanconi anemia, complementation group A)</OPTION><OPTION value="FBLN5">FBLN5 (fibulin 5)</OPTION><OPTION value="FBXL17">FBXL17 (F-box and leucine-rich repeat protein 17)</OPTION><OPTION value="FGFR3">FGFR3 (fibroblast growth factor receptor 3)</OPTION><OPTION value="FKRP">FKRP (fukutin related protein)</OPTION><OPTION value="FKTN">FKTN (fukutin)</OPTION><OPTION value="FLVCR1">FLVCR1 (feline leukemia virus subgroup C cellular receptor 1)</OPTION><OPTION value="FSCN2">FSCN2 (fascin homolog 2, actin-bundling protein, retinal (Strongylocen...))</OPTION><OPTION value="FZD4">FZD4 (frizzled family receptor 4)</OPTION><OPTION value="GAS8">GAS8 (growth arrest-specific 8)</OPTION><OPTION value="GIGYF2">GIGYF2 (GRB10 interacting GYF protein 2)</OPTION><OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION><OPTION value="GNAT1">GNAT1 (guanine nucleotide binding protein (G protein), alpha transducin...)</OPTION><OPTION value="GNAT2">GNAT2 (guanine nucleotide binding protein (G protein), alpha transducin...)</OPTION><OPTION value="GNPTG">GNPTG (N-acetylglucosamine-1-phosphate transferase, gamma subunit)</OPTION><OPTION value="GPR143">GPR143 (G protein-coupled receptor 143)</OPTION><OPTION value="GPR179">GPR179 (G protein-coupled receptor 179)</OPTION><OPTION value="GPR98">GPR98 (G protein-coupled receptor 98)</OPTION><OPTION value="GRK1">GRK1 (G protein-coupled receptor kinase 1)</OPTION><OPTION value="GRM6">GRM6 (glutamate receptor, metabotropic 6)</OPTION><OPTION value="GRN">GRN (granulin)</OPTION><OPTION value="GUCA1A">GUCA1A (guanylate cyclase activator 1A (retina))</OPTION><OPTION value="GUCA1B">GUCA1B (guanylate cyclase activator 1B (retina))</OPTION><OPTION value="GUCY2D">GUCY2D (guanylate cyclase 2D, membrane (retina-specific))</OPTION><OPTION value="HARS">HARS (histidyl-tRNA synthetase)</OPTION><OPTION value="HERC2">HERC2 (HECT and RLD domain containing E3 ubiquitin protein ligase 2)</OPTION><OPTION value="HESX1">HESX1 (HESX homeobox 1)</OPTION><OPTION value="HMCN1">HMCN1 (hemicentin 1)</OPTION><OPTION value="HTRA1">HTRA1 (HtrA serine peptidase 1)</OPTION><OPTION value="IDH3B">IDH3B (isocitrate dehydrogenase 3 (NAD+) beta)</OPTION><OPTION value="IFT140">IFT140 (intraflagellar transport 140 homolog (Chlamydomonas))</OPTION><OPTION value="IFT80">IFT80 (intraflagellar transport 80 homolog (Chlamydomonas))</OPTION><OPTION value="IMPDH1">IMPDH1 (IMP (inosine 5\'-monophosphate) dehydrogenase 1)</OPTION><OPTION value="IMPG2">IMPG2 (interphotoreceptor matrix proteoglycan 2)</OPTION><OPTION value="INPP5E">INPP5E (inositol polyphosphate-5-phosphatase, 72 kDa)</OPTION><OPTION value="INVS">INVS (inversin)</OPTION><OPTION value="IQCB1">IQCB1 (IQ motif containing B1)</OPTION><OPTION value="IRF4">IRF4 (interferon regulatory factor 4)</OPTION><OPTION value="ISPD">ISPD (isoprenoid synthase domain containing)</OPTION><OPTION value="JAG1">JAG1 (jagged 1)</OPTION><OPTION value="KCNJ13">KCNJ13 (potassium inwardly-rectifying channel, subfamily J, member 13)</OPTION><OPTION value="KCNV2">KCNV2 (potassium channel, subfamily V, member 2)</OPTION><OPTION value="KCTD7">KCTD7 (potassium channel tetramerization domain containing 7)</OPTION><OPTION value="KIF11">KIF11 (kinesin family member 11)</OPTION><OPTION value="KLHL7">KLHL7 (kelch-like family member 7)</OPTION><OPTION value="LARGE">LARGE (like-glycosyltransferase)</OPTION><OPTION value="LCA5">LCA5 (Leber congenital amaurosis 5)</OPTION><OPTION value="LCAT">LCAT (lecithin-cholesterol acyltransferase)</OPTION><OPTION value="LRAT">LRAT (lecithin retinol acyltransferase (phosphatidylcholine--retinol O...))</OPTION><OPTION value="LRIT3">LRIT3 (leucine-rich repeat, immunoglobulin-like and transmembrane domai...)</OPTION><OPTION value="LRP1B">LRP1B (low density lipoprotein receptor-related protein 1B)</OPTION><OPTION value="LRP5">LRP5 (low density lipoprotein receptor-related protein 5)</OPTION><OPTION value="LZTFL1">LZTFL1 (leucine zipper transcription factor-like 1)</OPTION><OPTION value="MAK">MAK (male germ cell-associated kinase)</OPTION><OPTION value="MC1R">MC1R (melanocortin 1 receptor (alpha melanocyte stimulating hormone re...))</OPTION><OPTION value="MERTK">MERTK (c-mer proto-oncogene tyrosine kinase)</OPTION><OPTION value="MFN2">MFN2 (mitofusin 2)</OPTION><OPTION value="MFRP">MFRP (membrane frizzled-related protein)</OPTION><OPTION value="MFSD8">MFSD8 (major facilitator superfamily domain containing 8)</OPTION><OPTION value="MKKS">MKKS (McKusick-Kaufman syndrome)</OPTION><OPTION value="MKS1">MKS1 (Meckel syndrome, type 1)</OPTION><OPTION value="MSH4">MSH4 (mutS homolog 4)</OPTION><OPTION value="MTAP">MTAP (methylthioadenosine phosphorylase)</OPTION><OPTION value="MTTP">MTTP (microsomal triglyceride transfer protein)</OPTION><OPTION value="MYH9">MYH9 (myosin, heavy chain 9, non-muscle)</OPTION><OPTION value="MYO7A">MYO7A (myosin VIIA)</OPTION><OPTION value="MYPN">MYPN (myopalladin)</OPTION><OPTION value="NBAS">NBAS (neuroblastoma amplified sequence)</OPTION><OPTION value="NDP">NDP (Norrie disease (pseudoglioma))</OPTION><OPTION value="NEK4">NEK4 (NIMA-related kinase 4)</OPTION><OPTION value="NEK8">NEK8 (NIMA-related kinase 8)</OPTION><OPTION value="NMNAT1">NMNAT1 (nicotinamide nucleotide adenylyltransferase 1)</OPTION><OPTION value="NPHP1">NPHP1 (nephronophthisis 1 (juvenile))</OPTION><OPTION value="NPHP3">NPHP3 (nephronophthisis 3 (adolescent))</OPTION><OPTION value="NPHP4">NPHP4 (nephronophthisis 4)</OPTION><OPTION value="NPLOC4">NPLOC4 (nuclear protein localization 4 homolog (S. cerevisiae))</OPTION><OPTION value="NR2E3">NR2E3 (nuclear receptor subfamily 2, group E, member 3)</OPTION><OPTION value="NRL">NRL (neural retina leucine zipper)</OPTION><OPTION value="NUB1">NUB1 (negative regulator of ubiquitin-like proteins 1)</OPTION><OPTION value="NYX">NYX (nyctalopin)</OPTION><OPTION value="OAT">OAT (ornithine aminotransferase)</OPTION><OPTION value="OCA2">OCA2 (oculocutaneous albinism II)</OPTION><OPTION value="OFD1">OFD1 (oral-facial-digital syndrome 1)</OPTION><OPTION value="OPA1">OPA1 (optic atrophy 1 (autosomal dominant))</OPTION><OPTION value="OPA1-AS1">OPA1-AS1 (OPA1 antisense RNA 1)</OPTION><OPTION value="OPA3">OPA3 (optic atrophy 3 (autosomal recessive, with chorea and spastic pa...))</OPTION><OPTION value="OPN1LW">OPN1LW (opsin 1 (cone pigments), long-wave-sensitive)</OPTION><OPTION value="OPN1MW">OPN1MW (opsin 1 (cone pigments), medium-wave-sensitive)</OPTION><OPTION value="OPN1SW">OPN1SW (opsin 1 (cone pigments), short-wave-sensitive)</OPTION><OPTION value="OTX2">OTX2 (orthodenticle homeobox 2)</OPTION><OPTION value="PANK2">PANK2 (pantothenate kinase 2)</OPTION><OPTION value="PAX2">PAX2 (paired box 2)</OPTION><OPTION value="PAX6">PAX6 (paired box 6)</OPTION><OPTION value="PCDH15">PCDH15 (protocadherin-related 15)</OPTION><OPTION value="PDE6A">PDE6A (phosphodiesterase 6A, cGMP-specific, rod, alpha)</OPTION><OPTION value="PDE6B">PDE6B (phosphodiesterase 6B, cGMP-specific, rod, beta)</OPTION><OPTION value="PDE6C">PDE6C (phosphodiesterase 6C, cGMP-specific, cone, alpha prime)</OPTION><OPTION value="PDE6G">PDE6G (phosphodiesterase 6G, cGMP-specific, rod, gamma)</OPTION><OPTION value="PDE6H">PDE6H (phosphodiesterase 6H, cGMP-specific, cone, gamma)</OPTION><OPTION value="PDZD7">PDZD7 (PDZ domain containing 7)</OPTION><OPTION value="PEX1">PEX1 (peroxisomal biogenesis factor 1)</OPTION><OPTION value="PEX10">PEX10 (peroxisomal biogenesis factor 10)</OPTION><OPTION value="PEX14">PEX14 (peroxisomal biogenesis factor 14)</OPTION><OPTION value="PEX16">PEX16 (peroxisomal biogenesis factor 16)</OPTION><OPTION value="PEX19">PEX19 (peroxisomal biogenesis factor 19)</OPTION><OPTION value="PEX2">PEX2 (peroxisomal biogenesis factor 2)</OPTION><OPTION value="PEX5">PEX5 (peroxisomal biogenesis factor 5)</OPTION><OPTION value="PEX6">PEX6 (peroxisomal biogenesis factor 6)</OPTION><OPTION value="PEX7">PEX7 (peroxisomal biogenesis factor 7)</OPTION><OPTION value="PGK1">PGK1 (phosphoglycerate kinase 1)</OPTION><OPTION value="PHYH">PHYH (phytanoyl-CoA 2-hydroxylase)</OPTION><OPTION value="PITPNM3">PITPNM3 (PITPNM family member 3)</OPTION><OPTION value="PLA2G5">PLA2G5 (phospholipase A2, group V)</OPTION><OPTION value="POMGNT1">POMGNT1 (protein O-linked mannose N-acetylglucosaminyltransferase 1 (b...))</OPTION><OPTION value="POMT1">POMT1 (protein-O-mannosyltransferase 1)</OPTION><OPTION value="POMT2">POMT2 (protein-O-mannosyltransferase 2)</OPTION><OPTION value="PPT1">PPT1 (palmitoyl-protein thioesterase 1)</OPTION><OPTION value="PRCD">PRCD (progressive rod-cone degeneration)</OPTION><OPTION value="PRDM7">PRDM7 (PR domain containing 7)</OPTION><OPTION value="PROM1">PROM1 (prominin 1)</OPTION><OPTION value="PRPF3">PRPF3 (pre-mRNA processing factor 3)</OPTION><OPTION value="PRPF31">PRPF31 (pre-mRNA processing factor 31)</OPTION><OPTION value="PRPF6">PRPF6 (pre-mRNA processing factor 6)</OPTION><OPTION value="PRPF8">PRPF8 (pre-mRNA processing factor 8)</OPTION><OPTION value="PRPH2">PRPH2 (peripherin 2 (retinal degeneration, slow))</OPTION><OPTION value="RAB28">RAB28 (RAB28, member RAS oncogene family)</OPTION><OPTION value="RAX2">RAX2 (retina and anterior neural fold homeobox 2)</OPTION><OPTION value="RB1">RB1 (retinoblastoma 1)</OPTION><OPTION value="RBP3">RBP3 (retinol binding protein 3, interstitial)</OPTION><OPTION value="RBP4">RBP4 (retinol binding protein 4, plasma)</OPTION><OPTION value="RD3">RD3 (retinal degeneration 3)</OPTION><OPTION value="RDH12">RDH12 (retinol dehydrogenase 12 (all-trans/9-cis/11-cis))</OPTION><OPTION value="RDH5">RDH5 (retinol dehydrogenase 5 (11-cis/9-cis))</OPTION><OPTION value="RFTN1">RFTN1 (raftlin, lipid raft linker 1)</OPTION><OPTION value="RGR">RGR (retinal G protein coupled receptor)</OPTION><OPTION value="RGS9">RGS9 (regulator of G-protein signaling 9)</OPTION><OPTION value="RGS9BP">RGS9BP (regulator of G protein signaling 9 binding protein)</OPTION><OPTION value="RHO">RHO (rhodopsin)</OPTION><OPTION value="RIMS1">RIMS1 (regulating synaptic membrane exocytosis 1)</OPTION><OPTION value="RLBP1">RLBP1 (retinaldehyde binding protein 1)</OPTION><OPTION value="ROM1">ROM1 (retinal outer segment membrane protein 1)</OPTION><OPTION value="RP1">RP1 (retinitis pigmentosa 1 (autosomal dominant))</OPTION><OPTION value="RP1L1">RP1L1 (retinitis pigmentosa 1-like 1)</OPTION><OPTION value="RP2">RP2 (retinitis pigmentosa 2 (X-linked recessive))</OPTION><OPTION value="RP9">RP9 (retinitis pigmentosa 9 (autosomal dominant))</OPTION><OPTION value="RPE65">RPE65 (retinal pigment epithelium-specific protein 65kDa)</OPTION><OPTION value="RPGR">RPGR (retinitis pigmentosa GTPase regulator)</OPTION><OPTION value="RPGRIP1">RPGRIP1 (retinitis pigmentosa GTPase regulator interacting protein 1)</OPTION><OPTION value="RPGRIP1L">RPGRIP1L (RPGRIP1-like)</OPTION><OPTION value="RS1">RS1 (retinoschisin 1)</OPTION><OPTION value="SAG">SAG (S-antigen; retina and pineal gland (arrestin))</OPTION><OPTION value="SCFD2">SCFD2 (sec1 family domain containing 2)</OPTION><OPTION value="SDCCAG8">SDCCAG8 (serologically defined colon cancer antigen 8)</OPTION><OPTION value="SEMA4A">SEMA4A (sema domain, immunoglobulin domain (Ig), transmembrane domain ...)</OPTION><OPTION value="SLC12A4">SLC12A4 (solute carrier family 12 (potassium/chloride transporter), mem...)</OPTION><OPTION value="SLC24A1">SLC24A1 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC24A4">SLC24A4 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC24A5">SLC24A5 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC45A2">SLC45A2 (solute carrier family 45, member 2)</OPTION><OPTION value="SNRNP200">SNRNP200 (small nuclear ribonucleoprotein 200kDa (U5))</OPTION><OPTION value="SOX2">SOX2 (SRY (sex determining region Y)-box 2)</OPTION><OPTION value="SOX2-OT">SOX2-OT (SOX2 overlapping transcript (non-protein coding))</OPTION><OPTION value="SPATA2L">SPATA2L (spermatogenesis associated 2-like)</OPTION><OPTION value="SPATA7">SPATA7 (spermatogenesis associated 7)</OPTION><OPTION value="SPG7">SPG7 (spastic paraplegia 7 (pure and complicated autosomal recessive))</OPTION><OPTION value="SPIRE2">SPIRE2 (spire-type actin nucleation factor 2)</OPTION><OPTION value="TEAD1">TEAD1 (TEA domain family member 1 (SV40 transcriptional enhancer factor))</OPTION><OPTION value="TIMM8A">TIMM8A (translocase of inner mitochondrial membrane 8 homolog A (yeast))</OPTION><OPTION value="TIMP3">TIMP3 (TIMP metallopeptidase inhibitor 3)</OPTION><OPTION value="TLR3">TLR3 (toll-like receptor 3)</OPTION><OPTION value="TLR4">TLR4 (toll-like receptor 4)</OPTION><OPTION value="TMEM126A">TMEM126A (transmembrane protein 126A)</OPTION><OPTION value="TMEM231">TMEM231 (transmembrane protein 231)</OPTION><OPTION value="TMEM237">TMEM237 (transmembrane protein 237)</OPTION><OPTION value="TMEM5">TMEM5 (transmembrane protein 5)</OPTION><OPTION value="TMEM67">TMEM67 (transmembrane protein 67)</OPTION><OPTION value="TOPORS">TOPORS (topoisomerase I binding, arginine/serine-rich, E3 ubiquitin pro...)</OPTION><OPTION value="TPCN2">TPCN2 (two pore segment channel 2)</OPTION><OPTION value="TPP1">TPP1 (tripeptidyl peptidase I)</OPTION><OPTION value="TREX1">TREX1 (three prime repair exonuclease 1)</OPTION><OPTION value="TRIM32">TRIM32 (tripartite motif containing 32)</OPTION><OPTION value="TRPM1">TRPM1 (transient receptor potential cation channel, subfamily M, member 1)</OPTION><OPTION value="TSHR">TSHR (thyroid stimulating hormone receptor)</OPTION><OPTION value="TSPAN12">TSPAN12 (tetraspanin 12)</OPTION><OPTION value="TTC21B">TTC21B (tetratricopeptide repeat domain 21B)</OPTION><OPTION value="TTC3">TTC3 (tetratricopeptide repeat domain 3)</OPTION><OPTION value="TTC8">TTC8 (tetratricopeptide repeat domain 8)</OPTION><OPTION value="TTPA">TTPA (tocopherol (alpha) transfer protein)</OPTION><OPTION value="TTR">TTR (transthyretin)</OPTION><OPTION value="TUBGCP6">TUBGCP6 (tubulin, gamma complex associated protein 6)</OPTION><OPTION value="TULP1">TULP1 (tubby like protein 1)</OPTION><OPTION value="TWIST1">TWIST1 (twist family bHLH transcription factor 1)</OPTION><OPTION value="TYR">TYR (tyrosinase)</OPTION><OPTION value="TYRP1">TYRP1 (tyrosinase-related protein 1)</OPTION><OPTION value="UCHL1">UCHL1 (ubiquitin carboxyl-terminal esterase L1 (ubiquitin thiolesterase))</OPTION><OPTION value="UNC119">UNC119 (unc-119 homolog (C. elegans))</OPTION><OPTION value="USH1C">USH1C (Usher syndrome 1C (autosomal recessive, severe))</OPTION><OPTION value="USH1G">USH1G (Usher syndrome 1G (autosomal recessive))</OPTION><OPTION value="USH2A">USH2A (Usher syndrome 2A (autosomal recessive, mild))</OPTION><OPTION value="VCAN">VCAN (versican)</OPTION><OPTION value="VPS13B">VPS13B (vacuolar protein sorting 13 homolog B (yeast))</OPTION><OPTION value="WDPCP">WDPCP (WD repeat containing planar cell polarity effector)</OPTION><OPTION value="WDR19">WDR19 (WD repeat domain 19)</OPTION><OPTION value="WFS1">WFS1 (Wolfram syndrome 1 (wolframin))</OPTION><OPTION value="WHAMMP2">WHAMMP2 (WAS protein homolog associated with actin, golgi membranes and...)</OPTION><OPTION value="ZNF276">ZNF276 (zinc finger protein 276)</OPTION><OPTION value="ZNF423">ZNF423 (zinc finger protein 423)</OPTION><OPTION value="ZNF513">ZNF513 (zinc finger protein 513)</OPTION><OPTION value="ZNF778">ZNF778 (zinc finger protein 778)</OPTION></SELECT><INPUT type="submit" value="Switch"></FORM>';
      document.getElementById('gene_name').innerHTML=sForm;
    }

    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jeegoocontext/jquery.jeegoocontext.min.js"> </SCRIPT>
  <LINK rel="stylesheet" type="text/css" href="lib/jeegoocontext/style.css">
  <LINK rel="stylesheet" type="text/css" href="lib/jQuery/css/cupertino/jquery-ui.custom.css">
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD valign="top" width="424" height="105">
      <IMG src="gfx/GEDI.png" alt="LOVD - Leiden Open Variation Database" width="404" height="100">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">The Genetic Eye Disorder (GEDI) Variation Database</H2>
      <H5 id="gene_name">CTS telomere maintenance complex component 1 (CTC1)&nbsp;<A href="#" onclick="lovd_switchGeneInline(); return false;"><IMG src="gfx/lovd_genes_switch_inline.png" width="23" height="23" alt="Switch gene" title="Switch gene database" align="top"></A></H5>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.3.0 Build 08 [ <A href="status">Current LOVD status</A> ]<BR>
      <A href="users?register"><B>Register as submitter</B></A> | <A href="login"><B>Log in</B></A>
    </TD>
  </TR>
  <TR>
    <TD width="150">&nbsp;</TD>
    <TD valign="top" colspan="2" style="padding-bottom : 2px;"><B>Curator: <A href="mailto:Shen_Lishuang@yahoo.com">Lishuang Shen</A></B></TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('gfx/tab_fill.png'); background-repeat : repeat-x;">
      <IMG src="gfx/tab_0F.png" alt="" width="25" height="25" align="left">
      <A href="genes/CTC1"><IMG src="gfx/tab_genes_F.png" alt="CTC1 homepage" id="tab_genes" width="44" height="25" align="left"></A>
      <IMG src="gfx/tab_FB.png" alt="" width="25" height="25" align="left">
      <A href="transcripts/CTC1"><IMG src="gfx/tab_transcripts_B.png" alt="View transcripts" id="tab_transcripts" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="variants/CTC1"><IMG src="gfx/tab_variants_B.png" alt="View variants" id="tab_variants" width="58" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="individuals/CTC1"><IMG src="gfx/tab_individuals_B.png" alt="View individuals" id="tab_individuals" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="diseases?search_genes_=CTC1"><IMG src="gfx/tab_diseases_B.png" alt="View diseases" id="tab_diseases" width="62" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="screenings/CTC1"><IMG src="gfx/tab_screenings_B.png" alt="View screenings" id="tab_screenings" width="78" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="submit"><IMG src="gfx/tab_submit_B.png" alt="Submit new data" id="tab_submit" width="53" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="docs"><IMG src="gfx/tab_docs_B.png" alt="LOVD documentation" id="tab_docs" width="110" height="25" align="left"></A>
      <IMG src="gfx/tab_B0.png" alt="" width="25" height="25" align="left">
    </TD>
  </TR>
</TABLE>

<IMG src="gfx/trans.png" alt="" width="792" height="0">

<!-- Start drop down menu definitions -->
<UL id="menu_tab_genes" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/genes"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genes</A></LI>
  <LI class="icon"><A href="/GEDI/genes/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View the CTC1 gene homepage</A></LI>
  <LI class="icon"><A href="/GEDI/genes/CTC1/graphs"><SPAN class="icon" style="background-image: url(gfx/menu_graphs.png);"></SPAN>View graphs about the CTC1 gene database</A></LI>
</UL>

<UL id="menu_tab_transcripts" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/transcripts"><SPAN class="icon" style="background-image: url(gfx/menu_transcripts.png);"></SPAN>View all transcripts</A></LI>
  <LI class="icon"><A href="/GEDI/transcripts/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_transcripts.png);"></SPAN>View all transcripts of the CTC1 gene</A></LI>
</UL>

<UL id="menu_tab_variants" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/variants"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genomic variants</A></LI>
  <LI class="icon"><A href="/GEDI/variants/in_gene"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all variants affecting transcripts</A></LI>
  <LI class="icon"><A href="/GEDI/variants/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all variants in the CTC1 gene</A></LI>
  <LI class="icon"><A href="/GEDI/view/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>Full data view for the CTC1 gene</A></LI>
</UL>

<UL id="menu_tab_individuals" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/individuals"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all individuals</A></LI>
  <LI class="icon"><A href="/GEDI/individuals/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all individuals screened for CTC1</A></LI>
</UL>

<UL id="menu_tab_diseases" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/diseases"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all diseases</A></LI>
</UL>

<UL id="menu_tab_screenings" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/screenings"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all screenings</A></LI>
  <LI class="icon"><A href="/GEDI/screenings/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all screenings for the CTC1 gene</A></LI>
</UL>

<UL id="menu_tab_submit" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/submit"><SPAN class="icon" style="background-image: url(gfx/plus.png);"></SPAN>Submit new data</A></LI>
</UL>


<SCRIPT type="text/javascript">
  $(function(){
    var aMenuOptions = {
        widthOverflowOffset: 0,
        heightOverflowOffset: 1,
        startLeftOffset: -20,
        event: "mouseover",
        openBelowContext: true,
        autoHide: true,
        delay: 100,
        onSelect: function(e, context){
            if($(this).hasClass("disabled"))
            {
                return false;
            } else {
                window.location = $(this).find("a").attr("href");
                return false;
            }
        }
    };
    $('#tab_genes').jeegoocontext('menu_tab_genes', aMenuOptions);
    $('#tab_transcripts').jeegoocontext('menu_tab_transcripts', aMenuOptions);
    $('#tab_variants').jeegoocontext('menu_tab_variants', aMenuOptions);
    $('#tab_individuals').jeegoocontext('menu_tab_individuals', aMenuOptions);
    $('#tab_diseases').jeegoocontext('menu_tab_diseases', aMenuOptions);
    $('#tab_screenings').jeegoocontext('menu_tab_screenings', aMenuOptions);
    $('#tab_submit').jeegoocontext('menu_tab_submit', aMenuOptions);
  });
</SCRIPT>
<!-- End drop down menu definitions -->



<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD style="padding-top : 10px;">







      <H2 class="LOVD">View gene CTC1</H2>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="600" class="data">
        <TR>
          <TH colspan="2" class="S15" valign="top">General information</TH></TR>
        <TR>
          <TH valign="top">Gene&nbsp;symbol</TH>
          <TD>CTC1</TD></TR>
        <TR>
          <TH valign="top">Gene&nbsp;name</TH>
          <TD>CTS telomere maintenance complex component 1</TD></TR>
        <TR>
          <TH valign="top">Chromosome</TH>
          <TD>17</TD></TR>
        <TR>
          <TH valign="top">Chromosomal&nbsp;band</TH>
          <TD>p13.1</TD></TR>
        <TR>
          <TH valign="top">Imprinted</TH>
          <TD>Unknown</TD></TR>
        <TR>
          <TH valign="top">Genomic&nbsp;reference</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/nuccore/NC_000017.10" target="_blank">NC_000017.10</A></TD></TR>
        <TR>
          <TH valign="top">Transcript&nbsp;reference</TH>
          <TD><A href="transcripts/00764">NM_025099.5</A></TD></TR>
        <TR>
          <TH valign="top">Associated&nbsp;with&nbsp;diseases</TH>
          <TD>-</TD></TR>
        <TR>
          <TH valign="top">Citation&nbsp;reference(s)</TH>
          <TD>http://oculargenomics.meei.harvard.edu/index.php/gdt</TD></TR>
        <TR>
          <TH valign="top">Curators&nbsp;(1)</TH>
          <TD><B>Lishuang Shen</B></TD></TR>
        <TR>
          <TH valign="top">Total&nbsp;number&nbsp;of&nbsp;public&nbsp;variants&nbsp;reported</TH>
          <TD><A href="variants/CTC1?search_var_status=%3D%22Marked%22%7C%3D%22Public%22">10</A></TD></TR>
        <TR>
          <TH valign="top">Unique&nbsp;public&nbsp;DNA&nbsp;variants&nbsp;reported</TH>
          <TD>10</TD></TR>
        <TR>
          <TH valign="top">Individuals&nbsp;with&nbsp;public&nbsp;variants</TH>
          <TD></TD></TR>
        <TR>
          <TH valign="top">Hidden&nbsp;variants</TH>
          <TD>0</TD></TR>
        <TR>
          <TH valign="top">Date&nbsp;created</TH>
          <TD>December 11, 2013</TD></TR>
        <TR>
          <TH valign="top">Date&nbsp;last&nbsp;updated</TH>
          <TD>December 11, 2013</TD></TR>
        <TR>
          <TH valign="top">Version</TH>
          <TD><B>CTC1:131211</B></TD></TR></TABLE>


      <HR>
      <TABLE border="0" cellpadding="0" cellspacing="1" width="600" class="data">
        <TR>
          <TH colspan="2" class="S15" valign="top">Graphical displays and utilities</TH></TR>
        <TR>
          <TH valign="top">Graphs</TH>
          <TD><A href="genes/CTC1/graphs" class="hide">Graphs displaying summary information of all variants in the database</A> &raquo;</TD></TR>
        <TR>
          <TH valign="top">UCSC&nbsp;Genome&nbsp;Browser</TH>
          <TD>Show variants in the UCSC Genome Browser (<A href="http://genome.ucsc.edu/cgi-bin/hgTracks?clade=mammal&amp;org=Human&amp;db=hg19&amp;position=chr17:8128089-8151463&amp;hgt.customText=http%3A%2F%2Fmseqdr.lumc.edu%2FGEDI%2Fapi%2Frest%2Fvariants%2FCTC1%3Fformat%3Dtext%2Fbed" target="_blank">full view</A>, <A href="http://genome.ucsc.edu/cgi-bin/hgTracks?clade=mammal&amp;org=Human&amp;db=hg19&amp;position=chr17:8128089-8151463&amp;hgt.customText=http%3A%2F%2Fmseqdr.lumc.edu%2FGEDI%2Fapi%2Frest%2Fvariants%2FCTC1%3Fformat%3Dtext%2Fbed%26visibility%3D4" target="_blank">compact view</A>)</TD></TR>
        <TR>
          <TH valign="top">Ensembl&nbsp;Genome&nbsp;Browser</TH>
          <TD>Show variants in the Ensembl Genome Browser (<A href="http://www.ensembl.org/Homo_sapiens/Location/View?r=17:8128089-8151463;contigviewbottom=url:http%3A%2F%2Fmseqdr.lumc.edu%2FGEDI%2Fapi%2Frest%2Fvariants%2FCTC1%3Fformat%3Dtext%2Fbed%26name%3D%2FCTC1%20variants=labels" target="_blank">full view</A>, <A href="http://www.ensembl.org/Homo_sapiens/Location/View?r=17:8128089-8151463;contigviewbottom=url:http%3A%2F%2Fmseqdr.lumc.edu%2FGEDI%2Fapi%2Frest%2Fvariants%2FCTC1%3Fformat%3Dtext%2Fbed%26name%3D%2FCTC1%20variants=normal" target="_blank">compact view</A>)</TD></TR>
        <TR>
          <TH valign="top">NCBI&nbsp;Sequence&nbsp;Viewer</TH>
          <TD>Show distribution histogram of variants in the <A href="http://www.ncbi.nlm.nih.gov/projects/sviewer/?id=NC_000017.10&amp;v=8128039:8151513&amp;content=7&amp;url=http%3A%2F%2Fmseqdr.lumc.edu%2FGEDI%2Fapi%2Frest%2Fvariants%2FCTC1%3Fformat%3Dtext%2Fbed" target="_blank">NCBI Sequence Viewer</A></TD></TR></TABLE>


      <HR>
      <TABLE border="0" cellpadding="0" cellspacing="1" width="600" class="data">
        <TR>
          <TH colspan="2" class="S15" valign="top">Links to other resources</TH></TR>
        <TR>
          <TH valign="top">HGNC</TH>
          <TD><A href="http://www.genenames.org/data/hgnc_data.php?hgnc_id=26169" target="_blank">26169</A></TD></TR>
        <TR>
          <TH valign="top">Entrez&nbsp;Gene</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?db=gene&amp;cmd=Retrieve&amp;dopt=full_report&amp;list_uids=80169" target="_blank">80169</A></TD></TR>
        <TR>
          <TH valign="top">OMIM&nbsp;-&nbsp;Gene</TH>
          <TD><A href="http://www.omim.org/entry/613129" target="_blank">613129</A></TD></TR>
        <TR>
          <TH valign="top">HGMD</TH>
          <TD><A href="http://www.hgmd.cf.ac.uk/ac/gene.php?gene=CTC1" target="_blank">CTC1</A></TD></TR>
        <TR>
          <TH valign="top">GeneCards</TH>
          <TD><A href="http://www.genecards.org/cgi-bin/carddisp.pl?gene=CTC1" target="_blank">CTC1</A></TD></TR>
        <TR>
          <TH valign="top">GeneTests</TH>
          <TD><A href="http://www.ncbi.nlm.nih.gov/sites/GeneTests/lab/gene/CTC1" target="_blank">CTC1</A></TD></TR></TABLE>

<BR><BR>

      <H4 class="LOVD">Active transcripts</H4>

      <SCRIPT type="text/javascript" src="inc-js-viewlist.php?nohistory"> </SCRIPT>
      <SCRIPT type="text/javascript" src="inc-js-tooltip.php"> </SCRIPT>
      <FORM action="genes/CTC1" method="get" id="viewlistForm_Transcripts_for_G_VE" style="margin : 0px;" onsubmit="return false;">
        <INPUT type="hidden" name="viewlistid" value="Transcripts_for_G_VE">
        <INPUT type="hidden" name="object" value="Transcript">
        <INPUT type="hidden" name="id" value="0">
        <INPUT type="hidden" name="order" value="variants,DESC">
        <INPUT type="hidden" name="skip[geneid]" value="geneid">
        <INPUT type="hidden" name="search_geneid" value="=&quot;CTC1&quot;">
        <INPUT type="hidden" name="hidenav" value="true">

      <DIV id="viewlistDiv_Transcripts_for_G_VE">
      <DIV id="viewlistLegend_Transcripts_for_G_VE" title="Legend" style="display : none;">
        <H2 class="LOVD">Legend</H2>

        <I class="S11">Please note that a short description of a certain column can be displayed when you move your mouse cursor over the column's header and hold it still. Below, a more detailed description is shown per column.</I><BR><BR>

      </DIV>

      <TABLE border="0" cellpadding="0" cellspacing="1" class="data" id="viewlistTable_Transcripts_for_G_VE">
        <THEAD>
        <TR>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="70" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_id_"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='id_,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_id_" value="" title="ID field should contain..." style="width : 64px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="40" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_chromosome"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='chromosome,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Chr&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_chromosome" value="" title="Chr field should contain..." style="width : 34px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="300" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_name"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='name,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Name&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_name" value="" title="Name field should contain..." style="width : 294px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="120" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_id_ncbi"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='id_ncbi,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">NCBI&nbsp;ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_id_ncbi" value="" title="NCBI ID field should contain..." style="width : 114px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="120" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_id_protein_ncbi"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='id_protein_ncbi,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">NCBI&nbsp;Protein&nbsp;ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_id_protein_ncbi" value="" title="NCBI Protein ID field should contain..." style="width : 114px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH>
          <TH valign="top" class="ordered">
            <IMG src="gfx/trans.png" alt="" width="70" height="1" id="viewlistTable_Transcripts_for_G_VE_colwidth_variants"><BR>
            <DIV onclick="document.forms['viewlistForm_Transcripts_for_G_VE'].order.value='variants,ASC'; if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } lovd_AJAX_viewListSubmit('Transcripts_for_G_VE');" style="position : relative;">
              <IMG src="gfx/order_arrow_desc.png" alt="Descending" title="Descending" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Variants&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_variants" value="" title="Variants field should contain..." style="width : 64px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_Transcripts_for_G_VE'].page) { document.forms['viewlistForm_Transcripts_for_G_VE'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'Transcripts_for_G_VE\')', 0); }"></TH></TR></THEAD>
        <TR class="data" id="00764" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/transcripts/00764';">
          <TD><A href="transcripts/00764" class="hide">00764</A></TD>
          <TD>17</TD>
          <TD>CTS telomere maintenance complex component 1</TD>
          <TD>NM_025099.5</TD>
          <TD>NP_079375.3</TD>
          <TD class="ordered">10</TD></TR></TABLE>
      </DIV></FORM><BR>
      <SCRIPT type="text/javascript">
        // This has to be run when the document has finished loading everything, because only then can it get the proper width from IE7 and lower!
        $( function () {lovd_stretchInputs('Transcripts_for_G_VE');});
        check_list['Transcripts_for_G_VE'] = [];
      </SCRIPT>

<BR>

      <TABLE border="0" cellpadding="0" cellspacing="1" width="950" class="data">
        <TR>
          <TH class="S15">Copyright &amp; disclaimer</TH></TR>
        <TR class="S11">
          <TD>The contents of this LOVD database are the intellectual property of the respective curator(s). Any unauthorised use, copying, storage or distribution of this material without written permission from the curator(s) will lead to copyright infringement with possible ensuing litigation. Copyright &copy; 2013-2014. All Rights Reserved. For further details, refer to Directive 96/9/EC of the European Parliament and the Council of March 11 (1996) on the legal protection of databases.<BR><BR>We have used all reasonable efforts to ensure that the information displayed on these pages and contained in the databases is of high quality. We make no warranty, express or implied, as to its accuracy or that the information is fit for a particular purpose, and will not be held responsible for any consequences arising out of any inaccuracies or omissions. Individuals, organisations and companies which use this database do so on the understanding that no liability whatsoever either direct or indirect shall rest upon the curator(s) or any of their employees or agents for the effects of any product, process or method that may be produced or adopted by any part, notwithstanding that the formulation of such product, process or method may be based upon information here provided.</TD></TR></TABLE><BR>










    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/3.0/" target="_blank">LOVD v.3.0</A> Build 08<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_update_error_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>
<SCRIPT type="text/javascript">
  <!--

function lovd_mapVariants ()
{
    // This function requests the script that will do the actual work.

    // First unbind any onclick handlers on the status image.
    $("#mapping_progress").unbind();

    // Now request the script.
    $.get("ajax/map_variants.php", function (sResponse)
        {
            // The server responded successfully. Let's see what he's saying.
            aResponse = sResponse.split("\t");
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_" + aResponse[1] + (aResponse[1] == "preparing"? ".gif" : ".png"), "title": aResponse[2]});

            if (sResponse.indexOf("Notice") >= 0 || sResponse.indexOf("Warning") >= 0 || sResponse.indexOf("Error") >= 0 || sResponse.indexOf("Fatal") >= 0) {
                // Something went wrong while processing the request, don't try again.
                $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sResponse});
            } else if (aResponse[0] == "1") {
                // More variants to map. Re-call.
                setTimeout("lovd_mapVariants()", 50);
            } else {
                // No more variants to map. But allow the user to try.
                $("#mapping_progress").click(lovd_mapVariants);
            }
        }
    ).fail(function (oObject, sStatus)
        {
            // Something went wrong while contacting the server, don't try again.
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sStatus});
        }
    );
}
$("#mapping_progress").click(lovd_mapVariants);
$("#mapping_progress").attr("Title", "Mapping is temporarily suspended because of network problems on the last attempt. Click to retry.");
  // -->
</SCRIPT>

</BODY>
</HTML>
"""

CTC1_VARIANT_DATABASE_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">
<HTML lang="en_US">
<HEAD>
  <TITLE>View transcript variants in CTC1 - The Genetic Eye Disorder (GEDI) Variation Database</TITLE>
  <META http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <META name="author" content="LOVD development team, LUMC, Netherlands">
  <META name="generator" content="gPHPEdit / GIMP @ GNU/Linux (Ubuntu)">
  <BASE href="http://mseqdr.lumc.edu/GEDI/">
  <LINK rel="stylesheet" type="text/css" href="styles.css">
  <LINK rel="shortcut icon" href="favicon.ico" type="image/x-icon">

  <SCRIPT type="text/javascript" src="inc-js-openwindow.php"> </SCRIPT>
  <SCRIPT type="text/javascript" src="inc-js-toggle-visibility.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery.min.js"> </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jQuery/jquery-ui.custom.min.js"> </SCRIPT>

  <SCRIPT type="text/javascript">
    <!--

    var sURL = "/GEDI/variants/{{GENE}}";
    function lovd_switchGeneInline () {
      var sForm = '<FORM action="" id="SelectGeneDBInline" method="get" style="margin : 0px;" onsubmit="document.location.href=(sURL.replace(\'{{GENE}}\', $(this).children(\'select\').val())); return false;"><SELECT name="select_db" onchange="$(this).parent().submit();"><OPTION value="ABCA4">ABCA4 (ATP-binding cassette, sub-family A (ABC1), member 4)</OPTION><OPTION value="ABCC6">ABCC6 (ATP-binding cassette, sub-family C (CFTR/MRP), member 6)</OPTION><OPTION value="ABHD12">ABHD12 (abhydrolase domain containing 12)</OPTION><OPTION value="ADAM9">ADAM9 (ADAM metallopeptidase domain 9)</OPTION><OPTION value="ADAMTS18">ADAMTS18 (ADAM metallopeptidase with thrombospondin type 1 motif, 18)</OPTION><OPTION value="AFG3L1P">AFG3L1P (AFG3-like AAA ATPase 1, pseudogene)</OPTION><OPTION value="AHI1">AHI1 (Abelson helper integration site 1)</OPTION><OPTION value="AIP">AIP (aryl hydrocarbon receptor interacting protein)</OPTION><OPTION value="AIPL1">AIPL1 (aryl hydrocarbon receptor interacting protein-like 1)</OPTION><OPTION value="ALMS1">ALMS1 (Alstrom syndrome 1)</OPTION><OPTION value="ANKRD11">ANKRD11 (ankyrin repeat domain 11)</OPTION><OPTION value="ARL13B">ARL13B (ADP-ribosylation factor-like 13B)</OPTION><OPTION value="ARL6">ARL6 (ADP-ribosylation factor-like 6)</OPTION><OPTION value="ARMS2">ARMS2 (age-related maculopathy susceptibility 2)</OPTION><OPTION value="ASIP">ASIP (agouti signaling protein)</OPTION><OPTION value="ATOH7">ATOH7 (atonal homolog 7 (Drosophila))</OPTION><OPTION value="ATXN7">ATXN7 (ataxin 7)</OPTION><OPTION value="B3GALNT2">B3GALNT2 (beta-1,3-N-acetylgalactosaminyltransferase 2)</OPTION><OPTION value="B3GNT1">B3GNT1 (UDP-GlcNAc:betaGal beta-1,3-N-acetylglucosaminyltransferase 1)</OPTION><OPTION value="BBS1">BBS1 (Bardet-Biedl syndrome 1)</OPTION><OPTION value="BBS10">BBS10 (Bardet-Biedl syndrome 10)</OPTION><OPTION value="BBS12">BBS12 (Bardet-Biedl syndrome 12)</OPTION><OPTION value="BBS2">BBS2 (Bardet-Biedl syndrome 2)</OPTION><OPTION value="BBS4">BBS4 (Bardet-Biedl syndrome 4)</OPTION><OPTION value="BBS5">BBS5 (Bardet-Biedl syndrome 5)</OPTION><OPTION value="BBS7">BBS7 (Bardet-Biedl syndrome 7)</OPTION><OPTION value="BBS9">BBS9 (Bardet-Biedl syndrome 9)</OPTION><OPTION value="BEST1">BEST1 (bestrophin 1)</OPTION><OPTION value="C10orf105">C10orf105 (chromosome 10 open reading frame 105)</OPTION><OPTION value="C1QTNF5">C1QTNF5 (C1q and tumor necrosis factor related protein 5)</OPTION><OPTION value="C2">C2 (complement component 2)</OPTION><OPTION value="C2orf71">C2orf71 (chromosome 2 open reading frame 71)</OPTION><OPTION value="C3">C3 (complement component 3)</OPTION><OPTION value="C5orf42">C5orf42 (chromosome 5 open reading frame 42)</OPTION><OPTION value="C8orf37">C8orf37 (chromosome 8 open reading frame 37)</OPTION><OPTION value="CA4">CA4 (carbonic anhydrase IV)</OPTION><OPTION value="CABP4">CABP4 (calcium binding protein 4)</OPTION><OPTION value="CACNA1F">CACNA1F (calcium channel, voltage-dependent, L type, alpha 1F subunit)</OPTION><OPTION value="CACNA2D4">CACNA2D4 (calcium channel, voltage-dependent, alpha 2/delta subunit 4)</OPTION><OPTION value="CAPN5">CAPN5 (calpain 5)</OPTION><OPTION value="CC2D2A">CC2D2A (coiled-coil and C2 domain containing 2A)</OPTION><OPTION value="CDH23">CDH23 (cadherin-related 23)</OPTION><OPTION value="CDH3">CDH3 (cadherin 3, type 1, P-cadherin (placental))</OPTION><OPTION value="CDHR1">CDHR1 (cadherin-related family member 1)</OPTION><OPTION value="CDK10">CDK10 (cyclin-dependent kinase 10)</OPTION><OPTION value="CDKL5">CDKL5 (cyclin-dependent kinase-like 5)</OPTION><OPTION value="CENPBD1">CENPBD1 (CENPB DNA-binding domains containing 1)</OPTION><OPTION value="CEP164">CEP164 (centrosomal protein 164kDa)</OPTION><OPTION value="CEP290">CEP290 (centrosomal protein 290kDa)</OPTION><OPTION value="CEP41">CEP41 (centrosomal protein 41kDa)</OPTION><OPTION value="CERKL">CERKL (ceramide kinase-like)</OPTION><OPTION value="CFB">CFB (complement factor B)</OPTION><OPTION value="CFH">CFH (complement factor H)</OPTION><OPTION value="CHM">CHM (choroideremia (Rab escort protein 1))</OPTION><OPTION value="CHMP1A">CHMP1A (charged multivesicular body protein 1A)</OPTION><OPTION value="CIB2">CIB2 (calcium and integrin binding family member 2)</OPTION><OPTION value="CLN3">CLN3 (ceroid-lipofuscinosis, neuronal 3)</OPTION><OPTION value="CLN5">CLN5 (ceroid-lipofuscinosis, neuronal 5)</OPTION><OPTION value="CLN6">CLN6 (ceroid-lipofuscinosis, neuronal 6, late infantile, variant)</OPTION><OPTION value="CLN8">CLN8 (ceroid-lipofuscinosis, neuronal 8 (epilepsy, progressive with me...))</OPTION><OPTION value="CLRN1">CLRN1 (clarin 1)</OPTION><OPTION value="CNGA1">CNGA1 (cyclic nucleotide gated channel alpha 1)</OPTION><OPTION value="CNGA3">CNGA3 (cyclic nucleotide gated channel alpha 3)</OPTION><OPTION value="CNGB1">CNGB1 (cyclic nucleotide gated channel beta 1)</OPTION><OPTION value="CNGB3">CNGB3 (cyclic nucleotide gated channel beta 3)</OPTION><OPTION value="CNNM4">CNNM4 (cyclin M4)</OPTION><OPTION value="COL11A1">COL11A1 (collagen, type XI, alpha 1)</OPTION><OPTION value="COL2A1">COL2A1 (collagen, type II, alpha 1)</OPTION><OPTION value="COL9A1">COL9A1 (collagen, type IX, alpha 1)</OPTION><OPTION value="CPNE7">CPNE7 (copine VII)</OPTION><OPTION value="CRB1">CRB1 (crumbs homolog 1 (Drosophila))</OPTION><OPTION value="CRX">CRX (cone-rod homeobox)</OPTION><OPTION value="CTC1" selected>CTC1 (CTS telomere maintenance complex component 1)</OPTION><OPTION value="CYP1B1">CYP1B1 (cytochrome P450, family 1, subfamily B, polypeptide 1)</OPTION><OPTION value="CYP4V2">CYP4V2 (cytochrome P450, family 4, subfamily V, polypeptide 2)</OPTION><OPTION value="DBNDD1">DBNDD1 (dysbindin (dystrobrevin binding protein 1) domain containing 1)</OPTION><OPTION value="DENND2A">DENND2A (DENN/MADD domain containing 2A)</OPTION><OPTION value="DFNB31">DFNB31 (deafness, autosomal recessive 31)</OPTION><OPTION value="DHDDS">DHDDS (dehydrodolichyl diphosphate synthase)</OPTION><OPTION value="DPEP1">DPEP1 (dipeptidase 1 (renal))</OPTION><OPTION value="EFEMP1">EFEMP1 (EGF containing fibulin-like extracellular matrix protein 1)</OPTION><OPTION value="ELOVL4">ELOVL4 (ELOVL fatty acid elongase 4)</OPTION><OPTION value="ERCC6">ERCC6 (excision repair cross-complementing rodent repair deficiency, co...)</OPTION><OPTION value="ESRRG">ESRRG (estrogen-related receptor gamma)</OPTION><OPTION value="EYS">EYS (eyes shut homolog (Drosophila))</OPTION><OPTION value="FAM161A">FAM161A (family with sequence similarity 161, member A)</OPTION><OPTION value="FAM66B">FAM66B (family with sequence similarity 66, member B)</OPTION><OPTION value="FAM66E">FAM66E (family with sequence similarity 66, member E)</OPTION><OPTION value="FAM78B">FAM78B (family with sequence similarity 78, member B)</OPTION><OPTION value="FANCA">FANCA (Fanconi anemia, complementation group A)</OPTION><OPTION value="FBLN5">FBLN5 (fibulin 5)</OPTION><OPTION value="FBXL17">FBXL17 (F-box and leucine-rich repeat protein 17)</OPTION><OPTION value="FGFR3">FGFR3 (fibroblast growth factor receptor 3)</OPTION><OPTION value="FKRP">FKRP (fukutin related protein)</OPTION><OPTION value="FKTN">FKTN (fukutin)</OPTION><OPTION value="FLVCR1">FLVCR1 (feline leukemia virus subgroup C cellular receptor 1)</OPTION><OPTION value="FSCN2">FSCN2 (fascin homolog 2, actin-bundling protein, retinal (Strongylocen...))</OPTION><OPTION value="FZD4">FZD4 (frizzled family receptor 4)</OPTION><OPTION value="GAS8">GAS8 (growth arrest-specific 8)</OPTION><OPTION value="GIGYF2">GIGYF2 (GRB10 interacting GYF protein 2)</OPTION><OPTION value="GMPPB">GMPPB (GDP-mannose pyrophosphorylase B)</OPTION><OPTION value="GNAT1">GNAT1 (guanine nucleotide binding protein (G protein), alpha transducin...)</OPTION><OPTION value="GNAT2">GNAT2 (guanine nucleotide binding protein (G protein), alpha transducin...)</OPTION><OPTION value="GNPTG">GNPTG (N-acetylglucosamine-1-phosphate transferase, gamma subunit)</OPTION><OPTION value="GPR143">GPR143 (G protein-coupled receptor 143)</OPTION><OPTION value="GPR179">GPR179 (G protein-coupled receptor 179)</OPTION><OPTION value="GPR98">GPR98 (G protein-coupled receptor 98)</OPTION><OPTION value="GRK1">GRK1 (G protein-coupled receptor kinase 1)</OPTION><OPTION value="GRM6">GRM6 (glutamate receptor, metabotropic 6)</OPTION><OPTION value="GRN">GRN (granulin)</OPTION><OPTION value="GUCA1A">GUCA1A (guanylate cyclase activator 1A (retina))</OPTION><OPTION value="GUCA1B">GUCA1B (guanylate cyclase activator 1B (retina))</OPTION><OPTION value="GUCY2D">GUCY2D (guanylate cyclase 2D, membrane (retina-specific))</OPTION><OPTION value="HARS">HARS (histidyl-tRNA synthetase)</OPTION><OPTION value="HERC2">HERC2 (HECT and RLD domain containing E3 ubiquitin protein ligase 2)</OPTION><OPTION value="HESX1">HESX1 (HESX homeobox 1)</OPTION><OPTION value="HMCN1">HMCN1 (hemicentin 1)</OPTION><OPTION value="HTRA1">HTRA1 (HtrA serine peptidase 1)</OPTION><OPTION value="IDH3B">IDH3B (isocitrate dehydrogenase 3 (NAD+) beta)</OPTION><OPTION value="IFT140">IFT140 (intraflagellar transport 140 homolog (Chlamydomonas))</OPTION><OPTION value="IFT80">IFT80 (intraflagellar transport 80 homolog (Chlamydomonas))</OPTION><OPTION value="IMPDH1">IMPDH1 (IMP (inosine 5\'-monophosphate) dehydrogenase 1)</OPTION><OPTION value="IMPG2">IMPG2 (interphotoreceptor matrix proteoglycan 2)</OPTION><OPTION value="INPP5E">INPP5E (inositol polyphosphate-5-phosphatase, 72 kDa)</OPTION><OPTION value="INVS">INVS (inversin)</OPTION><OPTION value="IQCB1">IQCB1 (IQ motif containing B1)</OPTION><OPTION value="IRF4">IRF4 (interferon regulatory factor 4)</OPTION><OPTION value="ISPD">ISPD (isoprenoid synthase domain containing)</OPTION><OPTION value="JAG1">JAG1 (jagged 1)</OPTION><OPTION value="KCNJ13">KCNJ13 (potassium inwardly-rectifying channel, subfamily J, member 13)</OPTION><OPTION value="KCNV2">KCNV2 (potassium channel, subfamily V, member 2)</OPTION><OPTION value="KCTD7">KCTD7 (potassium channel tetramerization domain containing 7)</OPTION><OPTION value="KIF11">KIF11 (kinesin family member 11)</OPTION><OPTION value="KLHL7">KLHL7 (kelch-like family member 7)</OPTION><OPTION value="LARGE">LARGE (like-glycosyltransferase)</OPTION><OPTION value="LCA5">LCA5 (Leber congenital amaurosis 5)</OPTION><OPTION value="LCAT">LCAT (lecithin-cholesterol acyltransferase)</OPTION><OPTION value="LRAT">LRAT (lecithin retinol acyltransferase (phosphatidylcholine--retinol O...))</OPTION><OPTION value="LRIT3">LRIT3 (leucine-rich repeat, immunoglobulin-like and transmembrane domai...)</OPTION><OPTION value="LRP1B">LRP1B (low density lipoprotein receptor-related protein 1B)</OPTION><OPTION value="LRP5">LRP5 (low density lipoprotein receptor-related protein 5)</OPTION><OPTION value="LZTFL1">LZTFL1 (leucine zipper transcription factor-like 1)</OPTION><OPTION value="MAK">MAK (male germ cell-associated kinase)</OPTION><OPTION value="MC1R">MC1R (melanocortin 1 receptor (alpha melanocyte stimulating hormone re...))</OPTION><OPTION value="MERTK">MERTK (c-mer proto-oncogene tyrosine kinase)</OPTION><OPTION value="MFN2">MFN2 (mitofusin 2)</OPTION><OPTION value="MFRP">MFRP (membrane frizzled-related protein)</OPTION><OPTION value="MFSD8">MFSD8 (major facilitator superfamily domain containing 8)</OPTION><OPTION value="MKKS">MKKS (McKusick-Kaufman syndrome)</OPTION><OPTION value="MKS1">MKS1 (Meckel syndrome, type 1)</OPTION><OPTION value="MSH4">MSH4 (mutS homolog 4)</OPTION><OPTION value="MTAP">MTAP (methylthioadenosine phosphorylase)</OPTION><OPTION value="MTTP">MTTP (microsomal triglyceride transfer protein)</OPTION><OPTION value="MYH9">MYH9 (myosin, heavy chain 9, non-muscle)</OPTION><OPTION value="MYO7A">MYO7A (myosin VIIA)</OPTION><OPTION value="MYPN">MYPN (myopalladin)</OPTION><OPTION value="NBAS">NBAS (neuroblastoma amplified sequence)</OPTION><OPTION value="NDP">NDP (Norrie disease (pseudoglioma))</OPTION><OPTION value="NEK4">NEK4 (NIMA-related kinase 4)</OPTION><OPTION value="NEK8">NEK8 (NIMA-related kinase 8)</OPTION><OPTION value="NMNAT1">NMNAT1 (nicotinamide nucleotide adenylyltransferase 1)</OPTION><OPTION value="NPHP1">NPHP1 (nephronophthisis 1 (juvenile))</OPTION><OPTION value="NPHP3">NPHP3 (nephronophthisis 3 (adolescent))</OPTION><OPTION value="NPHP4">NPHP4 (nephronophthisis 4)</OPTION><OPTION value="NPLOC4">NPLOC4 (nuclear protein localization 4 homolog (S. cerevisiae))</OPTION><OPTION value="NR2E3">NR2E3 (nuclear receptor subfamily 2, group E, member 3)</OPTION><OPTION value="NRL">NRL (neural retina leucine zipper)</OPTION><OPTION value="NUB1">NUB1 (negative regulator of ubiquitin-like proteins 1)</OPTION><OPTION value="NYX">NYX (nyctalopin)</OPTION><OPTION value="OAT">OAT (ornithine aminotransferase)</OPTION><OPTION value="OCA2">OCA2 (oculocutaneous albinism II)</OPTION><OPTION value="OFD1">OFD1 (oral-facial-digital syndrome 1)</OPTION><OPTION value="OPA1">OPA1 (optic atrophy 1 (autosomal dominant))</OPTION><OPTION value="OPA1-AS1">OPA1-AS1 (OPA1 antisense RNA 1)</OPTION><OPTION value="OPA3">OPA3 (optic atrophy 3 (autosomal recessive, with chorea and spastic pa...))</OPTION><OPTION value="OPN1LW">OPN1LW (opsin 1 (cone pigments), long-wave-sensitive)</OPTION><OPTION value="OPN1MW">OPN1MW (opsin 1 (cone pigments), medium-wave-sensitive)</OPTION><OPTION value="OPN1SW">OPN1SW (opsin 1 (cone pigments), short-wave-sensitive)</OPTION><OPTION value="OTX2">OTX2 (orthodenticle homeobox 2)</OPTION><OPTION value="PANK2">PANK2 (pantothenate kinase 2)</OPTION><OPTION value="PAX2">PAX2 (paired box 2)</OPTION><OPTION value="PAX6">PAX6 (paired box 6)</OPTION><OPTION value="PCDH15">PCDH15 (protocadherin-related 15)</OPTION><OPTION value="PDE6A">PDE6A (phosphodiesterase 6A, cGMP-specific, rod, alpha)</OPTION><OPTION value="PDE6B">PDE6B (phosphodiesterase 6B, cGMP-specific, rod, beta)</OPTION><OPTION value="PDE6C">PDE6C (phosphodiesterase 6C, cGMP-specific, cone, alpha prime)</OPTION><OPTION value="PDE6G">PDE6G (phosphodiesterase 6G, cGMP-specific, rod, gamma)</OPTION><OPTION value="PDE6H">PDE6H (phosphodiesterase 6H, cGMP-specific, cone, gamma)</OPTION><OPTION value="PDZD7">PDZD7 (PDZ domain containing 7)</OPTION><OPTION value="PEX1">PEX1 (peroxisomal biogenesis factor 1)</OPTION><OPTION value="PEX10">PEX10 (peroxisomal biogenesis factor 10)</OPTION><OPTION value="PEX14">PEX14 (peroxisomal biogenesis factor 14)</OPTION><OPTION value="PEX16">PEX16 (peroxisomal biogenesis factor 16)</OPTION><OPTION value="PEX19">PEX19 (peroxisomal biogenesis factor 19)</OPTION><OPTION value="PEX2">PEX2 (peroxisomal biogenesis factor 2)</OPTION><OPTION value="PEX5">PEX5 (peroxisomal biogenesis factor 5)</OPTION><OPTION value="PEX6">PEX6 (peroxisomal biogenesis factor 6)</OPTION><OPTION value="PEX7">PEX7 (peroxisomal biogenesis factor 7)</OPTION><OPTION value="PGK1">PGK1 (phosphoglycerate kinase 1)</OPTION><OPTION value="PHYH">PHYH (phytanoyl-CoA 2-hydroxylase)</OPTION><OPTION value="PITPNM3">PITPNM3 (PITPNM family member 3)</OPTION><OPTION value="PLA2G5">PLA2G5 (phospholipase A2, group V)</OPTION><OPTION value="POMGNT1">POMGNT1 (protein O-linked mannose N-acetylglucosaminyltransferase 1 (b...))</OPTION><OPTION value="POMT1">POMT1 (protein-O-mannosyltransferase 1)</OPTION><OPTION value="POMT2">POMT2 (protein-O-mannosyltransferase 2)</OPTION><OPTION value="PPT1">PPT1 (palmitoyl-protein thioesterase 1)</OPTION><OPTION value="PRCD">PRCD (progressive rod-cone degeneration)</OPTION><OPTION value="PRDM7">PRDM7 (PR domain containing 7)</OPTION><OPTION value="PROM1">PROM1 (prominin 1)</OPTION><OPTION value="PRPF3">PRPF3 (pre-mRNA processing factor 3)</OPTION><OPTION value="PRPF31">PRPF31 (pre-mRNA processing factor 31)</OPTION><OPTION value="PRPF6">PRPF6 (pre-mRNA processing factor 6)</OPTION><OPTION value="PRPF8">PRPF8 (pre-mRNA processing factor 8)</OPTION><OPTION value="PRPH2">PRPH2 (peripherin 2 (retinal degeneration, slow))</OPTION><OPTION value="RAB28">RAB28 (RAB28, member RAS oncogene family)</OPTION><OPTION value="RAX2">RAX2 (retina and anterior neural fold homeobox 2)</OPTION><OPTION value="RB1">RB1 (retinoblastoma 1)</OPTION><OPTION value="RBP3">RBP3 (retinol binding protein 3, interstitial)</OPTION><OPTION value="RBP4">RBP4 (retinol binding protein 4, plasma)</OPTION><OPTION value="RD3">RD3 (retinal degeneration 3)</OPTION><OPTION value="RDH12">RDH12 (retinol dehydrogenase 12 (all-trans/9-cis/11-cis))</OPTION><OPTION value="RDH5">RDH5 (retinol dehydrogenase 5 (11-cis/9-cis))</OPTION><OPTION value="RFTN1">RFTN1 (raftlin, lipid raft linker 1)</OPTION><OPTION value="RGR">RGR (retinal G protein coupled receptor)</OPTION><OPTION value="RGS9">RGS9 (regulator of G-protein signaling 9)</OPTION><OPTION value="RGS9BP">RGS9BP (regulator of G protein signaling 9 binding protein)</OPTION><OPTION value="RHO">RHO (rhodopsin)</OPTION><OPTION value="RIMS1">RIMS1 (regulating synaptic membrane exocytosis 1)</OPTION><OPTION value="RLBP1">RLBP1 (retinaldehyde binding protein 1)</OPTION><OPTION value="ROM1">ROM1 (retinal outer segment membrane protein 1)</OPTION><OPTION value="RP1">RP1 (retinitis pigmentosa 1 (autosomal dominant))</OPTION><OPTION value="RP1L1">RP1L1 (retinitis pigmentosa 1-like 1)</OPTION><OPTION value="RP2">RP2 (retinitis pigmentosa 2 (X-linked recessive))</OPTION><OPTION value="RP9">RP9 (retinitis pigmentosa 9 (autosomal dominant))</OPTION><OPTION value="RPE65">RPE65 (retinal pigment epithelium-specific protein 65kDa)</OPTION><OPTION value="RPGR">RPGR (retinitis pigmentosa GTPase regulator)</OPTION><OPTION value="RPGRIP1">RPGRIP1 (retinitis pigmentosa GTPase regulator interacting protein 1)</OPTION><OPTION value="RPGRIP1L">RPGRIP1L (RPGRIP1-like)</OPTION><OPTION value="RS1">RS1 (retinoschisin 1)</OPTION><OPTION value="SAG">SAG (S-antigen; retina and pineal gland (arrestin))</OPTION><OPTION value="SCFD2">SCFD2 (sec1 family domain containing 2)</OPTION><OPTION value="SDCCAG8">SDCCAG8 (serologically defined colon cancer antigen 8)</OPTION><OPTION value="SEMA4A">SEMA4A (sema domain, immunoglobulin domain (Ig), transmembrane domain ...)</OPTION><OPTION value="SLC12A4">SLC12A4 (solute carrier family 12 (potassium/chloride transporter), mem...)</OPTION><OPTION value="SLC24A1">SLC24A1 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC24A4">SLC24A4 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC24A5">SLC24A5 (solute carrier family 24 (sodium/potassium/calcium exchanger),...)</OPTION><OPTION value="SLC45A2">SLC45A2 (solute carrier family 45, member 2)</OPTION><OPTION value="SNRNP200">SNRNP200 (small nuclear ribonucleoprotein 200kDa (U5))</OPTION><OPTION value="SOX2">SOX2 (SRY (sex determining region Y)-box 2)</OPTION><OPTION value="SOX2-OT">SOX2-OT (SOX2 overlapping transcript (non-protein coding))</OPTION><OPTION value="SPATA2L">SPATA2L (spermatogenesis associated 2-like)</OPTION><OPTION value="SPATA7">SPATA7 (spermatogenesis associated 7)</OPTION><OPTION value="SPG7">SPG7 (spastic paraplegia 7 (pure and complicated autosomal recessive))</OPTION><OPTION value="SPIRE2">SPIRE2 (spire-type actin nucleation factor 2)</OPTION><OPTION value="TEAD1">TEAD1 (TEA domain family member 1 (SV40 transcriptional enhancer factor))</OPTION><OPTION value="TIMM8A">TIMM8A (translocase of inner mitochondrial membrane 8 homolog A (yeast))</OPTION><OPTION value="TIMP3">TIMP3 (TIMP metallopeptidase inhibitor 3)</OPTION><OPTION value="TLR3">TLR3 (toll-like receptor 3)</OPTION><OPTION value="TLR4">TLR4 (toll-like receptor 4)</OPTION><OPTION value="TMEM126A">TMEM126A (transmembrane protein 126A)</OPTION><OPTION value="TMEM231">TMEM231 (transmembrane protein 231)</OPTION><OPTION value="TMEM237">TMEM237 (transmembrane protein 237)</OPTION><OPTION value="TMEM5">TMEM5 (transmembrane protein 5)</OPTION><OPTION value="TMEM67">TMEM67 (transmembrane protein 67)</OPTION><OPTION value="TOPORS">TOPORS (topoisomerase I binding, arginine/serine-rich, E3 ubiquitin pro...)</OPTION><OPTION value="TPCN2">TPCN2 (two pore segment channel 2)</OPTION><OPTION value="TPP1">TPP1 (tripeptidyl peptidase I)</OPTION><OPTION value="TREX1">TREX1 (three prime repair exonuclease 1)</OPTION><OPTION value="TRIM32">TRIM32 (tripartite motif containing 32)</OPTION><OPTION value="TRPM1">TRPM1 (transient receptor potential cation channel, subfamily M, member 1)</OPTION><OPTION value="TSHR">TSHR (thyroid stimulating hormone receptor)</OPTION><OPTION value="TSPAN12">TSPAN12 (tetraspanin 12)</OPTION><OPTION value="TTC21B">TTC21B (tetratricopeptide repeat domain 21B)</OPTION><OPTION value="TTC3">TTC3 (tetratricopeptide repeat domain 3)</OPTION><OPTION value="TTC8">TTC8 (tetratricopeptide repeat domain 8)</OPTION><OPTION value="TTPA">TTPA (tocopherol (alpha) transfer protein)</OPTION><OPTION value="TTR">TTR (transthyretin)</OPTION><OPTION value="TUBGCP6">TUBGCP6 (tubulin, gamma complex associated protein 6)</OPTION><OPTION value="TULP1">TULP1 (tubby like protein 1)</OPTION><OPTION value="TWIST1">TWIST1 (twist family bHLH transcription factor 1)</OPTION><OPTION value="TYR">TYR (tyrosinase)</OPTION><OPTION value="TYRP1">TYRP1 (tyrosinase-related protein 1)</OPTION><OPTION value="UCHL1">UCHL1 (ubiquitin carboxyl-terminal esterase L1 (ubiquitin thiolesterase))</OPTION><OPTION value="UNC119">UNC119 (unc-119 homolog (C. elegans))</OPTION><OPTION value="USH1C">USH1C (Usher syndrome 1C (autosomal recessive, severe))</OPTION><OPTION value="USH1G">USH1G (Usher syndrome 1G (autosomal recessive))</OPTION><OPTION value="USH2A">USH2A (Usher syndrome 2A (autosomal recessive, mild))</OPTION><OPTION value="VCAN">VCAN (versican)</OPTION><OPTION value="VPS13B">VPS13B (vacuolar protein sorting 13 homolog B (yeast))</OPTION><OPTION value="WDPCP">WDPCP (WD repeat containing planar cell polarity effector)</OPTION><OPTION value="WDR19">WDR19 (WD repeat domain 19)</OPTION><OPTION value="WFS1">WFS1 (Wolfram syndrome 1 (wolframin))</OPTION><OPTION value="WHAMMP2">WHAMMP2 (WAS protein homolog associated with actin, golgi membranes and...)</OPTION><OPTION value="ZNF276">ZNF276 (zinc finger protein 276)</OPTION><OPTION value="ZNF423">ZNF423 (zinc finger protein 423)</OPTION><OPTION value="ZNF513">ZNF513 (zinc finger protein 513)</OPTION><OPTION value="ZNF778">ZNF778 (zinc finger protein 778)</OPTION></SELECT><INPUT type="submit" value="Switch"></FORM>';
      document.getElementById('gene_name').innerHTML=sForm;
    }

    //-->
  </SCRIPT>
  <SCRIPT type="text/javascript" src="lib/jeegoocontext/jquery.jeegoocontext.min.js"> </SCRIPT>
  <LINK rel="stylesheet" type="text/css" href="lib/jeegoocontext/style.css">
  <LINK rel="stylesheet" type="text/css" href="lib/jQuery/css/cupertino/jquery-ui.custom.css">
</HEAD>

<BODY style="margin : 0px;">

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%"><TR><TD>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD valign="top" width="424" height="105">
      <IMG src="gfx/GEDI.png" alt="LOVD - Leiden Open Variation Database" width="404" height="100">
    </TD>
    <TD valign="top" style="padding-top : 2px;">
      <H2 style="margin-bottom : 2px;">The Genetic Eye Disorder (GEDI) Variation Database</H2>
      <H5 id="gene_name">CTS telomere maintenance complex component 1 (CTC1)&nbsp;<A href="#" onclick="lovd_switchGeneInline(); return false;"><IMG src="gfx/lovd_genes_switch_inline.png" width="23" height="23" alt="Switch gene" title="Switch gene database" align="top"></A></H5>
    </TD>
    <TD valign="top" align="right" style="padding-right : 5px; padding-top : 2px;">
      LOVD v.3.0 Build 08 [ <A href="status">Current LOVD status</A> ]<BR>
      <A href="users?register"><B>Register as submitter</B></A> | <A href="login"><B>Log in</B></A>
    </TD>
  </TR>
  <TR>
    <TD width="150">&nbsp;</TD>
    <TD valign="top" colspan="2" style="padding-bottom : 2px;"><B>Curator: <A href="mailto:Shen_Lishuang@yahoo.com">Lishuang Shen</A></B></TD>
  </TR>
</TABLE>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="logo">
  <TR>
    <TD align="left" style="background : url('gfx/tab_fill.png'); background-repeat : repeat-x;">
      <IMG src="gfx/tab_0B.png" alt="" width="25" height="25" align="left">
      <A href="genes/CTC1"><IMG src="gfx/tab_genes_B.png" alt="CTC1 homepage" id="tab_genes" width="44" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="transcripts/CTC1"><IMG src="gfx/tab_transcripts_B.png" alt="View transcripts" id="tab_transcripts" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BF.png" alt="" width="25" height="25" align="left">
      <A href="variants/CTC1"><IMG src="gfx/tab_variants_F.png" alt="View variants" id="tab_variants" width="58" height="25" align="left"></A>
      <IMG src="gfx/tab_FB.png" alt="" width="25" height="25" align="left">
      <A href="individuals/CTC1"><IMG src="gfx/tab_individuals_B.png" alt="View individuals" id="tab_individuals" width="81" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="diseases?search_genes_=CTC1"><IMG src="gfx/tab_diseases_B.png" alt="View diseases" id="tab_diseases" width="62" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="screenings/CTC1"><IMG src="gfx/tab_screenings_B.png" alt="View screenings" id="tab_screenings" width="78" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="submit"><IMG src="gfx/tab_submit_B.png" alt="Submit new data" id="tab_submit" width="53" height="25" align="left"></A>
      <IMG src="gfx/tab_BB.png" alt="" width="25" height="25" align="left">
      <A href="docs"><IMG src="gfx/tab_docs_B.png" alt="LOVD documentation" id="tab_docs" width="110" height="25" align="left"></A>
      <IMG src="gfx/tab_B0.png" alt="" width="25" height="25" align="left">
    </TD>
  </TR>
</TABLE>

<IMG src="gfx/trans.png" alt="" width="792" height="0">

<!-- Start drop down menu definitions -->
<UL id="menu_tab_genes" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/genes"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genes</A></LI>
  <LI class="icon"><A href="/GEDI/genes/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View the CTC1 gene homepage</A></LI>
  <LI class="icon"><A href="/GEDI/genes/CTC1/graphs"><SPAN class="icon" style="background-image: url(gfx/menu_graphs.png);"></SPAN>View graphs about the CTC1 gene database</A></LI>
</UL>

<UL id="menu_tab_transcripts" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/transcripts"><SPAN class="icon" style="background-image: url(gfx/menu_transcripts.png);"></SPAN>View all transcripts</A></LI>
  <LI class="icon"><A href="/GEDI/transcripts/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_transcripts.png);"></SPAN>View all transcripts of the CTC1 gene</A></LI>
</UL>

<UL id="menu_tab_variants" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/variants"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all genomic variants</A></LI>
  <LI class="icon"><A href="/GEDI/variants/in_gene"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all variants affecting transcripts</A></LI>
  <LI class="icon"><A href="/GEDI/variants/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all variants in the CTC1 gene</A></LI>
  <LI class="icon"><A href="/GEDI/view/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>Full data view for the CTC1 gene</A></LI>
</UL>

<UL id="menu_tab_individuals" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/individuals"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all individuals</A></LI>
  <LI class="icon"><A href="/GEDI/individuals/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all individuals screened for CTC1</A></LI>
</UL>

<UL id="menu_tab_diseases" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/diseases"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all diseases</A></LI>
</UL>

<UL id="menu_tab_screenings" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/screenings"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all screenings</A></LI>
  <LI class="icon"><A href="/GEDI/screenings/CTC1"><SPAN class="icon" style="background-image: url(gfx/menu_magnifying_glass.png);"></SPAN>View all screenings for the CTC1 gene</A></LI>
</UL>

<UL id="menu_tab_submit" class="jeegoocontext">
  <LI class="icon"><A href="/GEDI/submit"><SPAN class="icon" style="background-image: url(gfx/plus.png);"></SPAN>Submit new data</A></LI>
</UL>


<SCRIPT type="text/javascript">
  $(function(){
    var aMenuOptions = {
        widthOverflowOffset: 0,
        heightOverflowOffset: 1,
        startLeftOffset: -20,
        event: "mouseover",
        openBelowContext: true,
        autoHide: true,
        delay: 100,
        onSelect: function(e, context){
            if($(this).hasClass("disabled"))
            {
                return false;
            } else {
                window.location = $(this).find("a").attr("href");
                return false;
            }
        }
    };
    $('#tab_genes').jeegoocontext('menu_tab_genes', aMenuOptions);
    $('#tab_transcripts').jeegoocontext('menu_tab_transcripts', aMenuOptions);
    $('#tab_variants').jeegoocontext('menu_tab_variants', aMenuOptions);
    $('#tab_individuals').jeegoocontext('menu_tab_individuals', aMenuOptions);
    $('#tab_diseases').jeegoocontext('menu_tab_diseases', aMenuOptions);
    $('#tab_screenings').jeegoocontext('menu_tab_screenings', aMenuOptions);
    $('#tab_submit').jeegoocontext('menu_tab_submit', aMenuOptions);
  });
</SCRIPT>
<!-- End drop down menu definitions -->



<DIV style="padding : 0px 10px;">
<TABLE border="0" cellpadding="0" cellspacing="0" width="100%">
  <TR>
    <TD style="padding-top : 10px;">







      <H2 class="LOVD">View transcript variants in CTC1</H2>

      <TABLE border="0" cellpadding="2" cellspacing="0" width="100%" class="info">
        <TR>
          <TD valign="top" align="center" width="40"><IMG src="gfx/lovd_information.png" alt="Information" title="Information" width="32" height="32" style="margin : 4px;"></TD>
          <TD valign="middle">The variants shown are described using the NM_025099.5 transcript reference sequence.</TD></TR></TABLE><BR>

      <SCRIPT type="text/javascript" src="inc-js-viewlist.php"> </SCRIPT>
      <SCRIPT type="text/javascript" src="inc-js-tooltip.php"> </SCRIPT>
      <FORM action="variants/CTC1" method="get" id="viewlistForm_CustomVL_VOT_VOG_CTC1" style="margin : 0px;" onsubmit="return false;">
        <INPUT type="hidden" name="viewlistid" value="CustomVL_VOT_VOG_CTC1">
        <INPUT type="hidden" name="object" value="Custom_ViewList">
        <INPUT type="hidden" name="object_id" value="VariantOnTranscript,VariantOnGenome">
        <INPUT type="hidden" name="id" value="CTC1">
        <INPUT type="hidden" name="order" value="VariantOnTranscript/DNA,ASC">
        <INPUT type="hidden" name="skip[chromosome]" value="chromosome">
        <INPUT type="hidden" name="skip[allele_]" value="allele_">
        <INPUT type="hidden" name="skip[transcriptid]" value="transcriptid">
        <INPUT type="hidden" name="search_transcriptid" value="00764">

      <DIV id="viewlistDiv_CustomVL_VOT_VOG_CTC1">
      <DIV id="viewlistLegend_CustomVL_VOT_VOG_CTC1" title="Legend" style="display : none;">
        <H2 class="LOVD">Legend</H2>

        <I class="S11">Please note that a short description of a certain column can be displayed when you move your mouse cursor over the column's header and hold it still. Below, a more detailed description is shown per column.</I><BR><BR>

        <B>Effect</B>: The variant's affect on the protein's function, in the format Reported/Curator concluded; '+' indicating the variant affects function, '+?' probably affects function, '-' does not affect function, '-?' probably does not affect function, '?' effect unknown.<BR><BR>

        <B>Exon</B>: Number of exon/intron containing variant; 2 = exon 2, 12i = intron 12, 2i_7i = exons 3 to 7, 8i_9 = border intron 8/exon 9.<BR><BR>

        <B>DNA change (cDNA)</B>: Description of variant at DNA level, based on a coding DNA reference sequence (following HGVS recommendations); e.g. c.123C>T, c.123_145del, c.123_126dup.<BR><BR>

        <B>RNA change</B>: Description of variant at RNA level (following HGVS recommendations).<BR>
<UL style="margin-top : 0px;">
  <LI>r.123c>u</LI>
  <LI>r.? = unknown</LI>
  <LI>r.(?) = RNA not analysed but probably transcribed copy of DNA variant</LI>
  <LI>r.spl? = RNA not analysed but variant probably affects splicing</LI>
  <LI>r.(spl?) = RNA not analysed but variant may affect splicing</LI>
  <LI>r.0? = change expected to abolish transcription</LI>
</UL>

        <B>Protein</B>: Description of variant at protein level (following HGVS recommendations).<BR>
<UL style="margin-top : 0px;">
  <LI>p.(Arg345Pro) = change predicted from DNA (RNA not analysed)</LI>
  <LI>p.Arg345Pro = change derived from RNA analysis</LI>
  <LI>p.? = unknown effect</LI>
  <LI>p.0? = probably no protein produced</LI>
</UL>

        <B>Allele</B>: On which allele is the variant located? Does not necessarily imply inheritance! 'Paternal' (confirmed or inferred), 'Maternal' (confirmed or inferred), 'Parent #1' or #2 for compound heterozygosity without having screened the parents, 'Unknown' for heterozygosity without having screened the parents, 'Both' for homozygozity.<BR><BR>

        <B>DNA change (genomic)</B>: Description of variant at DNA level, based on the genomic DNA reference sequence (following HGVS recommendations).<BR>
<UL style="margin-top : 0px;">
  <LI>g.12345678C>T</LI>
  <LI>g.12345678_12345890del</LI>
  <LI>g.12345678_12345890dup</LI>
</UL>

        <B>Reference</B>: Reference to publication describing the variant, including links to OMIM (when available), PubMed or or other source, e.g. "den Dunnen ASHG2003 P2346".<BR><BR>

        <B>DB-ID</B>: Database ID of variant, grouping multiple observations of the same variant together, starting with the HGNC gene symbol, followed by an underscore (_) and a six digit number (e.g. DMD_012345). _000000 is used for variants where DNA was not analysed (change predicted from RNA analysis), variants seen in animal models or variants not seen in humans but functionally tested in vitro.<BR><BR>

        <B>dbSNP ID</B>: The dbSNP ID.<BR><BR>

        <B>Frequency</B>: Frequency in which the variant was found; e.g 5/760 chromosomes (in 5 of 760 chromosomes tested), 1/33 patients (in 1 of 33 patients analysed in study), 0.05 controls (in 5% of control cases tested).<BR><BR>

        <B>iNote</B>: User's free text annotation<BR><BR>

      </DIV>

      <SPAN class="S11" id="viewlistPageSplitText_CustomVL_VOT_VOG_CTC1">
        10 entries on 1 page. Showing entries 1 - 10.
      </SPAN>
      <TABLE border="0" cellpadding="0" cellspacing="3" class="pagesplit_nav">
        <TR>
          <TD style="border : 0px; cursor : default; padding-right : 10px;">
            <SELECT onchange="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page_size.value = this.value; document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value = 1; lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');">
              <OPTION value="10">10 per page</OPTION>
              <OPTION value="25">25 per page</OPTION>
              <OPTION value="50">50 per page</OPTION>
              <OPTION value="100" selected>100 per page</OPTION>
              <OPTION value="250">250 per page</OPTION>
              <OPTION value="500">500 per page</OPTION>
              <OPTION value="1000">1000 per page</OPTION>
            </SELECT></TD>
          <TD><B onclick="lovd_showLegend('CustomVL_VOT_VOG_CTC1');" title="Click here to see the full legend of this data table." class="legend">Legend</B>&nbsp;&nbsp;</TD></TR></TABLE>

      <TABLE border="0" cellpadding="0" cellspacing="1" class="data" id="viewlistTable_CustomVL_VOT_VOG_CTC1">
        <THEAD>
        <TR>
          <TH valign="top" class="order" title="The variant's effect on the protein's function, in the format Reported/Curator concluded; ranging from '+' (variant affects function) to '-' (does not affect function).">
            <IMG src="gfx/trans.png" alt="" width="70" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_vot_effect"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='vot_effect,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Effect&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_vot_effect" value="" title="Effect field should contain..." style="width : 64px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order" title="Number of exon/intron containing the variant.">
            <IMG src="gfx/trans.png" alt="" width="50" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnTranscript/Exon"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnTranscript/Exon,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Exon&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnTranscript/Exon" value="" title="Exon field should contain..." style="width : 44px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="ordered" title="Description of variant at DNA level, based on a coding DNA reference sequence (following HGVS recommendations).">
            <IMG src="gfx/trans.png" alt="" width="200" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnTranscript/DNA"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnTranscript/DNA,DESC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow_asc.png" alt="Ascending" title="Ascending" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">DNA&nbsp;change&nbsp;(cDNA)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnTranscript/DNA" value="" title="DNA change (cDNA) field should contain..." style="width : 194px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order" title="Description of variant at RNA level (following HGVS recommendations).">
            <IMG src="gfx/trans.png" alt="" width="200" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnTranscript/RNA"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnTranscript/RNA,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">RNA&nbsp;change&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnTranscript/RNA" value="" title="RNA change field should contain..." style="width : 194px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order" title="Description of variant at protein level (following HGVS recommendations).">
            <IMG src="gfx/trans.png" alt="" width="200" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnTranscript/Protein"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnTranscript/Protein,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Protein&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnTranscript/Protein" value="" title="Protein field should contain..." style="width : 194px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order" title="Description of variant at DNA level, based on the genomic DNA reference sequence (following HGVS recommendations).">
            <IMG src="gfx/trans.png" alt="" width="200" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnGenome/DNA"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnGenome/DNA,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">DNA&nbsp;change&nbsp;(genomic)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnGenome/DNA" value="" title="DNA change (genomic) field should contain..." style="width : 194px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order" title="Reference to publication describing the variant.">
            <IMG src="gfx/trans.png" alt="" width="200" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnGenome/Reference"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnGenome/Reference,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Reference&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnGenome/Reference" value="" title="Reference field should contain..." style="width : 194px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order" title="Database ID of variant starting with the HGNC gene symbol, followed by an underscore (_) and a six digit number (e.g. DMD_012345). _000000 is used for variants where DNA was not analysed (change predicted from RNA analysis), variants seen in animal models or variants not seen in humans but functionally tested in vitro.">
            <IMG src="gfx/trans.png" alt="" width="120" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnGenome/DBID"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnGenome/DBID,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">DB-ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnGenome/DBID" value="" title="DB-ID field should contain..." style="width : 114px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order" title="The dbSNP ID.">
            <IMG src="gfx/trans.png" alt="" width="120" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnGenome/dbSNP"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnGenome/dbSNP,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">dbSNP&nbsp;ID&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnGenome/dbSNP" value="" title="dbSNP ID field should contain..." style="width : 114px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order" title="Frequency in which the variant was found; e.g 5/760 chromosomes (in 5 of 760 chromosomes tested), 1/33 patients (in 1 of 33 patients analysed in study), 0.05 controls (in 5% of control cases tested).">
            <IMG src="gfx/trans.png" alt="" width="90" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnGenome/Frequency"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnGenome/Frequency,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Frequency&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnGenome/Frequency" value="" title="Frequency field should contain..." style="width : 84px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order" title="User's free text annotation">
            <IMG src="gfx/trans.png" alt="" width="200" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_VariantOnGenome/iNote"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='VariantOnGenome/iNote,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">iNote&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_VariantOnGenome/iNote" value="" title="iNote field should contain..." style="width : 194px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH>
          <TH valign="top" class="order">
            <IMG src="gfx/trans.png" alt="" width="160" height="1" id="viewlistTable_CustomVL_VOT_VOG_CTC1_colwidth_owned_by_"><BR>
            <DIV onclick="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].order.value='owned_by_,ASC'; if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');" style="position : relative;">
              <IMG src="gfx/order_arrow.png" alt="" title="" width="13" height="12" style="position : absolute; top : 2px; right : 0px;">Owner&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DIV>
            <INPUT type="text" name="search_owned_by_" value="" title="Owner field should contain..." style="width : 154px; font-weight : normal;" onkeydown="if (event.keyCode == 13) { if (document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page) { document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value=1; } setTimeout('lovd_AJAX_viewListSubmit(\'CustomVL_VOT_VOG_CTC1\')', 0); }"></TH></TR></THEAD>
        <TR class="marked" id="0000000777" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000777#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.680C&gt;T</TD>
          <TD>r.(?)</TD>
          <TD>p.(Ala227Val)</TD>
          <TD>g.8140805G&gt;A</TD>
          <TD>-</TD>
          <TD>CTC1_000002</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs199473673" target="_blank">rs199473673</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR>
        <TR class="marked" id="0000000966" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000966#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.775G&gt;A</TD>
          <TD>r.(?)</TD>
          <TD>p.(Val259Met)</TD>
          <TD>g.8140710C&gt;T</TD>
          <TD>-</TD>
          <TD>CTC1_000001</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs387907080" target="_blank">rs387907080</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR>
        <TR class="marked" id="0000000973" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000973#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.859C&gt;T</TD>
          <TD>r.(?)</TD>
          <TD>p.(Arg287*)</TD>
          <TD>g.8139594G&gt;A</TD>
          <TD>-</TD>
          <TD>CTC1_000004</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs397514660" target="_blank">rs397514660</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR>
        <TR class="marked" id="0000000778" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000778#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.1994T&gt;G</TD>
          <TD>r.(?)</TD>
          <TD>p.(Val665Gly)</TD>
          <TD>g.8135745A&gt;C</TD>
          <TD>-</TD>
          <TD>CTC1_000003</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs199473676" target="_blank">rs199473676</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR>
        <TR class="marked" id="0000000914" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000914#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.2518C&gt;T</TD>
          <TD>r.(?)</TD>
          <TD>p.(Arg840Trp)</TD>
          <TD>g.8134745G&gt;A</TD>
          <TD>-</TD>
          <TD>CTC1_000010</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs373905859" target="_blank">rs373905859</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR>
        <TR class="marked" id="0000000913" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000913#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.2611G&gt;A</TD>
          <TD>r.(?)</TD>
          <TD>p.(Val871Met)</TD>
          <TD>g.8134652C&gt;T</TD>
          <TD>-</TD>
          <TD>CTC1_000009</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs369255297" target="_blank">rs369255297</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR>
        <TR class="marked" id="0000000813" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000813#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.2959C&gt;T</TD>
          <TD>r.(?)</TD>
          <TD>p.(Arg987Trp)</TD>
          <TD>g.8133261G&gt;A</TD>
          <TD>-</TD>
          <TD>CTC1_000008</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs202138550" target="_blank">rs202138550</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR>
        <TR class="marked" id="0000000811" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000811#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.3425T&gt;A</TD>
          <TD>r.(?)</TD>
          <TD>p.(Leu1142His)</TD>
          <TD>g.8131910A&gt;T</TD>
          <TD>-</TD>
          <TD>CTC1_000007</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs201455840" target="_blank">rs201455840</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR>
        <TR class="marked" id="0000000810" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000810#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.3425T&gt;C</TD>
          <TD>r.(?)</TD>
          <TD>p.(Leu1142Pro)</TD>
          <TD>g.8131910A&gt;G</TD>
          <TD>-</TD>
          <TD>CTC1_000006</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs201455840" target="_blank">rs201455840</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR>
        <TR class="marked" id="0000000779" valign="top" style="cursor : pointer;" onclick="window.location.href = '/GEDI/variants/0000000779#00764';">
          <TD>?/?</TD>
          <TD>-</TD>
          <TD class="ordered">c.3583C&gt;T</TD>
          <TD>r.(?)</TD>
          <TD>p.(Arg1195*)</TD>
          <TD>g.8131569G&gt;A</TD>
          <TD>-</TD>
          <TD>CTC1_000005</TD>
          <TD><SPAN onclick="cancelParentEvent(event);"><A href="http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs199473682" target="_blank">rs199473682</A></SPAN></TD>
          <TD>-</TD>
          <TD>-</TD>
          <TD><SPAN class="custom_link" onmouseover="lovd_showToolTip('<TABLE border=0 cellpadding=0 cellspacing=0 width=350 class=S11><TR><TH valign=top>User&nbsp;ID</TH><TD>00001</TD></TR><TR><TH valign=top>Name</TH><TD>Lishuang Shen</TD></TR><TR><TH valign=top>Email&nbsp;address</TH><TD>&#083;&#104;&#101;&#110;&#095;&#076;&#105;&#115;&#104;&#117;&#097;&#110;&#103;&#064;&#121;&#097;&#104;&#111;&#111;&#046;&#099;&#111;&#109;</TD></TR><TR><TH valign=top>Institute</TH><TD>MEEI</TD></TR><TR><TH valign=top>Department</TH><TD></TD></TR><TR><TH valign=top>Country</TH><TD>US</TD></TR></TABLE>', this, [-200, 0]);">Lishuang Shen</SPAN></TD></TR></TABLE>
        <INPUT type="hidden" name="total" value="10" disabled>
        <INPUT type="hidden" name="page_size" value="100">
        <INPUT type="hidden" name="page" value="1">

      <TABLE border="0" cellpadding="0" cellspacing="3" class="pagesplit_nav">
        <TR>
          <TD style="border : 0px; cursor : default; padding-right : 10px;">
            <SELECT onchange="document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page_size.value = this.value; document.forms['viewlistForm_CustomVL_VOT_VOG_CTC1'].page.value = 1; lovd_AJAX_viewListSubmit('CustomVL_VOT_VOG_CTC1');">
              <OPTION value="10">10 per page</OPTION>
              <OPTION value="25">25 per page</OPTION>
              <OPTION value="50">50 per page</OPTION>
              <OPTION value="100" selected>100 per page</OPTION>
              <OPTION value="250">250 per page</OPTION>
              <OPTION value="500">500 per page</OPTION>
              <OPTION value="1000">1000 per page</OPTION>
            </SELECT></TD>
          <TD><B onclick="lovd_showLegend('CustomVL_VOT_VOG_CTC1');" title="Click here to see the full legend of this data table." class="legend">Legend</B>&nbsp;&nbsp;</TD></TR></TABLE>

      </DIV></FORM><BR>
      <SCRIPT type="text/javascript">
        // This has to be run when the document has finished loading everything, because only then can it get the proper width from IE7 and lower!
        $( function () {lovd_stretchInputs('CustomVL_VOT_VOG_CTC1');});
        check_list['CustomVL_VOT_VOG_CTC1'] = [];
      </SCRIPT>










    </TD>
  </TR>
</TABLE>
</DIV>
<BR>

<TABLE border="0" cellpadding="0" cellspacing="0" width="100%" class="footer">
  <TR>
    <TD width="84">
      &nbsp;
    </TD>
    <TD align="center">
  Powered by <A href="http://www.LOVD.nl/3.0/" target="_blank">LOVD v.3.0</A> Build 08<BR>
  &copy;2004-2013 <A href="http://www.lumc.nl/" target="_blank">Leiden University Medical Center</A>
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_mapping_99.png" alt="" title="" width="32" height="32" id="mapping_progress" style="margin : 5px;">
    </TD>
    <TD width="42" align="right">
      <IMG src="gfx/lovd_update_error_blue.png" alt="" width="32" height="32" style="margin : 5px;">
    </TD>
  </TR>
</TABLE>

</TD></TR></TABLE>
<SCRIPT type="text/javascript">
  <!--

function lovd_mapVariants ()
{
    // This function requests the script that will do the actual work.

    // First unbind any onclick handlers on the status image.
    $("#mapping_progress").unbind();

    // Now request the script.
    $.get("ajax/map_variants.php", function (sResponse)
        {
            // The server responded successfully. Let's see what he's saying.
            aResponse = sResponse.split("\t");
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_" + aResponse[1] + (aResponse[1] == "preparing"? ".gif" : ".png"), "title": aResponse[2]});

            if (sResponse.indexOf("Notice") >= 0 || sResponse.indexOf("Warning") >= 0 || sResponse.indexOf("Error") >= 0 || sResponse.indexOf("Fatal") >= 0) {
                // Something went wrong while processing the request, don't try again.
                $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sResponse});
            } else if (aResponse[0] == "1") {
                // More variants to map. Re-call.
                setTimeout("lovd_mapVariants()", 50);
            } else {
                // No more variants to map. But allow the user to try.
                $("#mapping_progress").click(lovd_mapVariants);
            }
        }
    ).fail(function (oObject, sStatus)
        {
            // Something went wrong while contacting the server, don't try again.
            $("#mapping_progress").attr({"src": "gfx/lovd_mapping_99.png", "title": "There was a problem with LOVD while mapping variants to transcripts: " + sStatus});
        }
    );
}
$("#mapping_progress").click(lovd_mapVariants);
$("#mapping_progress").attr("Title", "Mapping is temporarily suspended because of network problems on the last attempt. Click to retry.");
  // -->
</SCRIPT>

</BODY>
</HTML>
"""

CTC1_TABLE_DATA = [['?/?', '-', 'c.680C>T', 'r.(?)', 'p.(Ala227Val)', 'g.8140805G>A', '-', 'CTC1_000002', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs199473673', '-', '-', 'Lishuang Shen'],
                   ['?/?', '-', 'c.775G>A', 'r.(?)', 'p.(Val259Met)', 'g.8140710C>T', '-', 'CTC1_000001', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs387907080', '-', '-', 'Lishuang Shen'],
                   ['?/?', '-', 'c.859C>T', 'r.(?)', 'p.(Arg287*)', 'g.8139594G>A', '-', 'CTC1_000004', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs397514660', '-', '-', 'Lishuang Shen'],
                   ['?/?', '-', 'c.1994T>G', 'r.(?)', 'p.(Val665Gly)', 'g.8135745A>C', '-', 'CTC1_000003', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs199473676', '-', '-', 'Lishuang Shen'],
                   ['?/?', '-', 'c.2518C>T', 'r.(?)', 'p.(Arg840Trp)', 'g.8134745G>A', '-', 'CTC1_000010', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs373905859', '-', '-', 'Lishuang Shen'],
                   ['?/?', '-', 'c.2611G>A', 'r.(?)', 'p.(Val871Met)', 'g.8134652C>T', '-', 'CTC1_000009', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs369255297', '-', '-', 'Lishuang Shen'],
                   ['?/?', '-', 'c.2959C>T', 'r.(?)', 'p.(Arg987Trp)', 'g.8133261G>A', '-', 'CTC1_000008', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs202138550', '-', '-', 'Lishuang Shen'],
                   ['?/?', '-', 'c.3425T>A', 'r.(?)', 'p.(Leu1142His)', 'g.8131910A>T', '-', 'CTC1_000007', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs201455840', '-', '-', 'Lishuang Shen'],
                   ['?/?', '-', 'c.3425T>C', 'r.(?)', 'p.(Leu1142Pro)', 'g.8131910A>G', '-', 'CTC1_000006', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs201455840', '-', '-', 'Lishuang Shen'],
                   ['?/?', '-', 'c.3583C>T', 'r.(?)', 'p.(Arg1195*)', 'g.8131569G>A', '-', 'CTC1_000005', 'http://www.ncbi.nlm.nih.gov/SNP/snp_ref.cgi?rs=rs199473682', '-', '-', 'Lishuang Shen']]
