<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
     <xsl:template match="/">
        <html>
            <head>
                <title>L'Amour et la Raison/Charles-Antoine-Guillaume Pigault de l'Épinoy</title>
            </head>
            <body>
				<h2>L'Amour et la Raison/Charles-Antoine-Guillaume Pigault de l'Épinoy</h2>
                <h2>Auteurs du projet : Laure Torello, Jeremy Chaumont, Chloé Luthier</h2>
                 <xsl:apply-templates/> 
            </body>
        </html>
    </xsl:template>
    
    <xsl:template match="/play/scene">
    <hr /> <xsl:apply-templates />
     <br/>
    </xsl:template>
    
    <xsl:template match="scene">
    <p style="color:blue" align="center"> Scene: <xsl:apply-templates /></p>
     <br/>
    </xsl:template>

    <xsl:template match="personnage|didascalie|replique">
    <hr /> <xsl:apply-templates />
     <br/>
    </xsl:template>
   
    <xsl:template match="personnage">
    <p style="color:purple"> Personnage: <xsl:apply-templates /></p>
     <br/>
    </xsl:template>
 
    <xsl:template match="didascalie">
     <i style="color:grey"> Didascalie: <xsl:apply-templates /></i>
     <br/>
    </xsl:template>

    <xsl:template match="replique">
     <p style="color:black"> Réplique: <xsl:apply-templates /></p>
     <br/>
    </xsl:template>
   
</xsl:stylesheet>