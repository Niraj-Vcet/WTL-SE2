<?xml version="1.0" encoding="UTF-8"?>

<xsl:stylesheet version="1.0"
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<xsl:template match="/">

<html>
<head>
    <title>Employee Management Report</title>

    <style>
        body {
            font-family: Arial;
        }

        h2 {
            color: darkblue;
        }

        table {
            border-collapse: collapse;
            width: 80%;
        }

        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }

        th {
            background-color: lightblue;
        }

        .highSalary {
            background-color: lightgreen;
        }

        .lowSalary {
            background-color: #ffcccc;
        }
    </style>
</head>

<body>

<h2>Employee Details</h2>

<table>
    <tr>
        <th>Emp ID</th>
        <th>Name</th>
        <th>Department</th>
        <th>Designation</th>
        <th>Salary</th>
        <th>Experience</th>
        <th>Status</th>
    </tr>

    <!-- Loop through employees -->
    <xsl:for-each select="company/employee">

        <!-- Sort by salary descending -->
        <xsl:sort select="salary" data-type="number" order="descending"/>

        <tr>

            <!-- Conditional Row Coloring -->
            <xsl:attribute name="class">
                <xsl:choose>
                    <xsl:when test="salary &gt; 70000">highSalary</xsl:when>
                    <xsl:otherwise>lowSalary</xsl:otherwise>
                </xsl:choose>
            </xsl:attribute>

            <td><xsl:value-of select="@empId"/></td>
            <td><xsl:value-of select="name"/></td>
            <td><xsl:value-of select="department"/></td>
            <td><xsl:value-of select="designation"/></td>
            <td><xsl:value-of select="salary"/></td>
            <td><xsl:value-of select="experience"/></td>

            <!-- Conditional Status -->
            <td>
                <xsl:choose>
                    <xsl:when test="experience &gt;= 5">
                        Senior
                    </xsl:when>
                    <xsl:otherwise>
                        Junior
                    </xsl:otherwise>
                </xsl:choose>
            </td>

        </tr>

    </xsl:for-each>

</table>

<br/>

<!-- Summary Section -->
<h3>Summary</h3>

<p>Total Employees: 
    <xsl:value-of select="count(company/employee)"/>
</p>


</body>

</html>

</xsl:template>

</xsl:stylesheet>